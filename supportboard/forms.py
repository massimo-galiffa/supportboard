from django import forms

from supportboard.models import SupportRequest
from .models import User


class SupportRequestForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titel der Anfrage'}))
    # description = forms.CharField(
    #     widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Beschreibung der Anfrage'}))
    # status = forms.CharField(
    #     widget=forms.Select(choices=SupportRequest.STATUS_CHOICES,
    #                         attrs={'class': 'form-control', 'placeholder': 'Status'}))
    # importance = forms.Select(choices=SupportRequest.IMPORTANCE_CHOICES,
    #                           attrs={'class': 'form-control', 'placeholder': 'Wichtigkeit'})

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
