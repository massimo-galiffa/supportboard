from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView

from .forms import SupportRequestForm
from .models import SupportRequest
from supportboard.forms import SupportRequestForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/authy/login')
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


@login_required(login_url='/authy/login')
def support_request_list(request):
    support_requests = SupportRequest.objects.all()
    return render(request, 'supportboard/support_request_list.html', {'support_requests': support_requests})


def support_request_delete(request, id):
    id = int(id)
    support_request = SupportRequest.objects.get(id=id)
    support_request.delete()
    return redirect('list')


def support_request_detail(request, pk):
    support_request = SupportRequest.objects.get(pk=pk)
    return render(request, 'supportboard/support_request_detail.html', {'support_request': support_request})


def support_request_update(request, pk):
    support_request = SupportRequest.objects.get(pk=pk)
    support_request.save()

    return HttpResponseRedirect(reverse('list'))
