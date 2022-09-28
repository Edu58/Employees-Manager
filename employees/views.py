from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    form = RegisterForm

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    
    return render(request, 'register.html', {'form': form})

def login_user(request):
    return render(request, 'login.html')
