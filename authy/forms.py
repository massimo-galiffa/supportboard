from django import forms
from django.contrib.auth.models import User


# Sign up form
class SignupForm(forms.ModelForm):
    # In input text
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Firstname...'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lastname...'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username..'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password...'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter password...'}))

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password', 'password2'
        ]


# Login form
class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


