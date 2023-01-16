# support request form
from django import forms

from supportboard.models import SupportRequest


class SupportRequestForm(forms.ModelForm):

    class Meta:
        model = SupportRequest
        fields = ['title', 'description',]

