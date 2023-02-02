from django import forms
from django.contrib.auth.models import User


# Sign up form
class SignupForm(forms.ModelForm):
    # # In input text
    # first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Firstname...'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lastname...'}))
    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username..'}))
    # email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email...'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password...'}))
    # group = forms.CharField(max_length=30, initial='Lernende', widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

