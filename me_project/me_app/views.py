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
    if(request.method == 'POST'):
        new_idea = Idea()
        new_idea.title = request.POST['title']
        new_idea.writer = request.POST['writer']
        new_idea.body = request.POST['body']
        new_idea.pud_date = timezone.now()
        new_idea.image = request.FILES['image']
        new_idea.save()
    return redirect('detail', new_idea.id)

def update(request, idea_id):
    if(request.method == 'POST'):
        edit_idea = get_object_or_404(Idea, pk=idea_id)
        edit_idea.title = request.POST['title']
        edit_idea.writer = request.POST['writer']
        edit_idea.body = request.POST['body']
        edit_idea.pud_date = timezone.now()
        edit_idea.image = request.FILES['image']
        edit_idea.save()
    return redirect('detail', edit_idea.id)

def delete(request, idea_id):
    delete_idea= get_object_or_404(Idea, pk=idea_id)
    delete_idea.delete()
    return redirect('main')

def detail(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    comments = Comment.objects.filter(idea = idea)
    return render(request, 'detail.html', {'idea': idea, 'comments' : comments})

def edit(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, 'edit.html', {'idea':idea})

def add_comment_to_idea(request, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    form = CommentForm()
    response = {
        'form': form,
        'idea_id': idea_id,
    }

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.idea = idea
            comment.save()
            return redirect('detail', idea.id)
    return render(request, 'add_comment_to_idea.html', response)