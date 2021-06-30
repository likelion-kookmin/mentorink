from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import UserModel

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                error_message = "에러"
        else:
            error_message = "가입하지 않은 아이디이거나, 잘못된 비밀번호입니다."

        return render(request, 'login.html', {'form': form, 'error': error_message})

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("main")


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if UserModel.objects.filter(username=request.POST['username']).exists():
            error = "이미 등록된 Username입니다"
            return render(request, 'signup.html', {'form': form, 'error': error})
        if request.POST['password1'] != request.POST['password2']:
            error = "비밀번호가 서로 다릅니다"
            return render(request, 'signup.html', {'form': form, 'error': error})
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect("main")

    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
