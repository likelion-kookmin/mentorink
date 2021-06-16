from .models import Idea
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .form import IdeaForm, CommentForm


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
    ideas = get_object_or_404(Idea, pk=id)
    return render(request, 'detail.html', {'ideas': ideas})

def add_comment_to_idea(request, pk):
    post = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_idea.html', {'form': form})