from django.contrib import admin
from .models import CustomUser, Department, Employee

# Register your models here.
admin.site.register([
    CustomUser,
    Department,
    Employee
])