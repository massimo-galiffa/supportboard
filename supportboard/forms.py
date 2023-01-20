from django import forms

from supportboard.models import SupportRequest
from .models import User


class SupportRequestForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    status = forms.CharField(widget=forms.Select(choices=SupportRequest.STATUS_CHOICES, attrs={'class': 'form-control'}))

    class Meta:
        model = SupportRequest
        fields = ['title', 'description', 'assigned_trainer']


class SupportRequestTrainerForm(forms.ModelForm):
    assigned_trainer = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Berufsbildner'),
                                              widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = SupportRequest
        fields = ['title', 'description', 'assigned_trainer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_trainer'].queryset = User.objects.filter(groups__name='berufsbildner')
