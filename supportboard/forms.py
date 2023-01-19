# support request form
from django import forms

from supportboard.models import SupportRequest


class SupportRequestForm(forms.ModelForm):
    class Meta:
        model = SupportRequest

        class SupportRequestForm(forms.Form):
            title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
            description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

        fields = ['title', 'description', ]
