from .models import CustomUser, Employee, Initial, Department
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

class AddInitialForm(forms.ModelForm):
    class Meta:
        model = Initial
        fields='__all__'

class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class AddDepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields= '__all__'