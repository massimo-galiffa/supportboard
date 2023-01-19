from django import forms
from supportboard.models import SupportRequest
from .models import User


class SupportRequestForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = SupportRequest
        fields = ['title', 'description', ]


class SupportRequestTrainerForm(forms.ModelForm):
    class Meta:
        model = SupportRequest
        fields = ['title', 'description', 'assigned_trainer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assigned_trainer'].queryset = User.objects.filter(groups__name='berufsbildner')
