from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

from authy.forms import SignupForm


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
    return render(request, 'supportboard/support_request_list.html')
