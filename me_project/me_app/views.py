from me_app.models import Idea
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

def main(request):
    return render(request, 'main.html')

def login(request):
    return render(request, 'login.html')

def join(request):
    return render(request, 'join.html')

def mypage(request):
    return render(request, 'mypage.html')

def list(request):
    return render(request, 'list.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    new_idea = Idea()
    new_idea.title = request.POST['title']
    new_idea.writer = request.POST['writer']
    new_idea.body = request.POST['body']
    new_idea.pud_date = timezone.now()
    new_idea.save()
    return redirect('detail',new_idea.id)