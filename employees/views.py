from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import RegisterForm, LoginUser, AddEmployeeForm, AddInitialForm, AddDepartmentForm
from .models import Department, Employee, Initial
from django.contrib.auth.decorators import login_required

# Create your views here.
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
            return redirect('home')

    return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def home(request):
    form = AddInitialForm
    initials = Initial.objects.all()

    if request.method == "POST":
        form = AddInitialForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'index.html', {'initials': initials, 'addinitialform': form})
    

@login_required(login_url='login')
def update_initial(request, id):
    initial = get_object_or_404(Initial, pk=id)

    form = AddInitialForm(instance=initial)

    if request.method == "POST":
        form = AddInitialForm(request.POST, instance=initial)

        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'update_initial.html', {'update_initial_form': form, 'initial': initial})

@login_required(login_url='login')
def delete_initial(request, id):
    initial = get_object_or_404(Initial, pk=id)

    if initial:
        initial.delete()
        return redirect('home')


@login_required(login_url='login')
def departments(request):
    form = AddDepartmentForm
    departments = Department.objects.all()

    if request.method == "POST":
        form = AddDepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('departments')

    return render(request, 'departments.html', {'departments': departments, 'add_department_form': form})

@login_required(login_url='login')
def update_department(request, id):
    department = get_object_or_404(Department, pk=id)

    form = AddDepartmentForm(instance=department)

    if request.method == "POST":
        form = AddDepartmentForm(request.POST, instance=department)

        if form.is_valid():
            form.save()
            return redirect('departments')
    
    return render(request, 'update_department.html', {'update_department_form': form, 'department': department})

@login_required(login_url='login')
def delete_department(request, id):
    department = get_object_or_404(Department, pk=id)

    if department:
        department.delete()
        return redirect('departments')

@login_required(login_url='login')
def employees(request):
    form = AddEmployeeForm
    employees = Employee.objects.all()

    if request.method == "POST":
        form = AddEmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employees')

    return render(request, 'employees.html', {'employees': employees, 'add_employee_form': form})

@login_required(login_url='login')
def update_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)

    form = AddEmployeeForm(instance=employee)

    if request.method == "POST":
        form = AddEmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employees')
    
    return render(request, 'update_employee.html', {'update_employee_form': form, 'employee': employee})

@login_required(login_url='login')
def delete_employee(request, id):
    employee = get_object_or_404(Employee, pk=id)

    if employee:
        employee.delete()
        return redirect('employees')