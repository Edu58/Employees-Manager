from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginUser

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
    form = LoginUser

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html', {'form': form})
