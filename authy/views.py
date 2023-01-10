from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from authy.forms import SignupForm, LoginForm
from django.contrib.auth.models import User


# Create your views here.


def signup(request):
    form = SignupForm
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(form.data["username"], form.data["email"], form.data["password"])
            user.save()
    return render(request, 'authy/login.html', {"form": form})


@login_required
def home(request):
    return render(request, 'authy/home.html')


def de(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            print(request, 'Username or password is incorrect')
    return render(request, 'authy/login.html')


def logged(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                return render(request, 'authy/login.html', {'error': 'Username or password is incorrect'})
    else:
        form = LoginForm()
    return render(request, 'authy/login.html', {'form': form})


# Loggout button
def loggout_user(request):
    logout(request)
    return redirect('login')


