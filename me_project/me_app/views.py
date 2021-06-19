from .models import Comment, Idea
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import CommentForm


def main(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'login.html')


def join(request):
    return render(request, 'join.html')


def mypage(request):
    return render(request, 'mypage.html')


def list(request):
    search = request.POST.get('search')
    ideas = Idea.objects.filter(title__contains=search)
    return render(request, 'list.html', {'ideas': ideas})


def new(request):
    return render(request, 'new.html')


def create(request):
    new_idea = Idea()
    new_idea.title = request.POST['title']
    new_idea.writer = request.POST['writer']
    new_idea.body = request.POST['body']
    new_idea.pud_date = timezone.now()
    new_idea.save()
    return redirect('detail', new_idea.id)


def detail(request, id):
    idea = get_object_or_404(Idea, pk=id)
    comments = Comment.objects.filter(post = idea)
    return render(request, 'detail.html', {'idea': idea, 'comments' : comments})

def add_comment_to_idea(request, idea_id):
    post = get_object_or_404(Idea, pk=idea_id)
    form = CommentForm()
    response = {
        'form': form,
        'idea_id': idea_id,
    }

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', post.id)
    return render(request, 'add_comment_to_idea.html', response)