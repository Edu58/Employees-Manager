from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'phone_number', 'username', 'password1', 'password2']