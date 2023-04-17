from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from supportboard.forms import SupportRequestForm
from .models import SupportRequest
from django.contrib import messages


@login_required(login_url='/accounts/login')
def support_request(request):
    form = SupportRequestForm()
    if request.method == 'POST':
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            # create or update the support request
            support_request = form.save(commit=False)
            support_request.creator = request.user
            support_request.save()
            return redirect('list')
        else:
            print(form.errors)
    return render(request, 'supportboard/support_request.html', {
        'form': form,
        'trainers': User.objects.filter(groups__name='Berufsbildner'),
        'importance_choices': SupportRequest.IMPORTANCE_CHOICES,
        'status_choices': SupportRequest.STATUS_CHOICES
    })


@login_required(login_url='/accounts/login')
def support_request_list(request):
    support_requests = SupportRequest.objects.all()
    messages.success(request, f'Hallo {request.user.username}!')
    return render(request, 'supportboard/support_request_list.html', {'support_requests': support_requests})


def support_request_delete(request, pk):
    support_request = SupportRequest.objects.get(id=id)
    if support_request.creator == request.user or request.user.groups.filter(name='Berufsbildner').exists():
        support_request.delete()
        return redirect('list')
    else:
        return redirect('detail', pk=pk)


def support_request_detail(request, pk):
    support_request = SupportRequest.objects.get(pk=pk)
    return render(request, 'supportboard/support_request_detail.html', {'support_request': support_request})


def update_support_request(request, pk):
    try:
        support_request_object = SupportRequest.objects.get(id=pk)
    except SupportRequest.DoesNotExist:
        return redirect('list')
    form = SupportRequestForm(instance=support_request_object)
    if request.method == 'POST':
        form = SupportRequestForm(request.POST, instance=support_request_object)
        if form.is_valid():
            form.save()
            return redirect('list')
    return render(request, 'supportboard/support_request.html', {
        'form': form,
        'trainers': User.objects.filter(groups__name='Berufsbildner'),
        'importance_choices': SupportRequest.IMPORTANCE_CHOICES,
        'status_choices': SupportRequest.STATUS_CHOICES
    })
