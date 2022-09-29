from django.contrib import admin
from .models import CustomUser, Department, Employee, Initial

# Register your models here.
admin.site.register([
    CustomUser,
    Department,
    Initial,
    Employee
])