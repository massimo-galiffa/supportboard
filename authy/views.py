from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authy.forms import SignupForm, LoginForm
from django.contrib.auth.models import User, Group


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.data["username"], form.data["email"], form.data["password"])
            group = Group.objects.get(name=form.cleaned_data.get('group'))
            user.groups.add(group)
            user.save()
            return redirect('login')
    return render(request, 'authy/signup.html', {"form": form})


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
            logged(request, user)
            return redirect('list')
        else:
            print(request, 'Username or password is incorrect')
    return render(request, 'authy/login.html')


def logged(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                return redirect('list')

    return render(request, 'authy/login.html', {'form': form})


# Loggout button
def loggout_user(request):
    logout(request)
    return redirect('login')
