from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from supportboard.forms import SupportRequestForm, SupportRequestTrainerForm
from .models import SupportRequest


@login_required(login_url='/accounts/login')
def support_request(request):
    if request.method == 'POST':
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            # create or update the support request
            support_request = form.save(commit=False)
            support_request.creator = request.user
            support_request.save()
            return HttpResponseRedirect('list')
    else:
        form = SupportRequestForm()
    return render(request, 'supportboard/support_request.html', {'form': form})


@login_required(login_url='/accounts/login')
def support_request_list(request):
    support_requests = SupportRequest.objects.all()
    return render(request, 'supportboard/support_request_list.html', {'support_requests': support_requests})


def support_request_delete(request, id):
    id = int(id)
    support_request = SupportRequest.objects.get(id=id)
    if support_request.creator == request.user or request.user.groups.filter(name='Berufsbildner').exists():
        support_request.delete()
        return redirect('list')
    else:
        return render(request, 'supportboard/support_request_detail.html', {'support_request': support_request})


def support_request_detail(request, pk):
    support_request = SupportRequest.objects.get(pk=pk)
    return render(request, 'supportboard/support_request_detail.html', {'support_request': support_request})


def support_request_update(request, pk):
    support_request = SupportRequest.objects.get(pk=pk)
    support_request.save()

    return HttpResponseRedirect(reverse('list'))


def update_support_request(request, pk):
    support_request = SupportRequest.objects.get(id=pk)
    if request.method == 'POST':
        form = SupportRequestForm(request.POST, instance=support_request)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = SupportRequestForm(instance=support_request)
    return render(request, 'supportboard/support_request.html', {'form': form})


def support_request_group(request):
    if request.method == 'POST':
        form = SupportRequestTrainerForm(request.POST)
        if form.is_valid():
            if request.user.groups.filter(name='Berufsbildner').exists():
                form.save()
                return redirect('success')
            else:
                return HttpResponse("You are not authorized to make changes to the assigned trainer")
    else:
        form = SupportRequestTrainerForm()
    return render(request, 'supportboard/support_request_detail.html', {'form': form})





