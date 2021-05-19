from django.shortcuts import render

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
