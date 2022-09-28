from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(help_text=None)
    password2 = forms.CharField(widget=forms.PasswordInput, help_text=None)
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'phone_number', 'username', 'password1', 'password2']


class LoginUser(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password']