from django.shortcuts import render, redirect
from .forms import SupportRequestForm
from .models import SupportRequest
from supportboard.forms import SupportRequestForm


def support_request(request):
    if request.method == 'POST':
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            # create or update the support request
            support_request = form.save(commit=False)
            support_request.creator = request.user
            support_request.save()
            return redirect('list')
    else:
        form = SupportRequestForm()
    return render(request, 'supportboard/support_request.html', {'form': form})


def support_request_list(request):
    support_requests = SupportRequest.objects.all()
    return render(request, 'supportboard/support_request_list.html', {'support_requests': support_requests})
