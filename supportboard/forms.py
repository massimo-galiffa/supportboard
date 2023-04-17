from django import forms

from supportboard.models import SupportRequest
from .models import User


class SupportRequestForm(forms.ModelForm):
    class Meta:
        model = SupportRequest
        exclude = ['creation_date', 'creator']


class SupportRequestTrainerForm(forms.ModelForm):
    assigned_trainer = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Berufsbildner'),
                                              widget=forms.Select(
                                                  attrs={'class': 'form-control', 'placeholder': 'Berufsbildner'}))

    class Meta:
        model = SupportRequest
        fields = ['title', 'description', 'assigned_trainer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_trainer'].queryset = User.objects.filter(groups__name='berufsbildner')
