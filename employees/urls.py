from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('update-initial/<id>', update_initial, name='update_initial'),
    path('delete-initial/<id>', delete_initial, name='delete_initial'),
    path('departments/', departments, name='departments'),
    path('update-department/<id>', update_department, name='update_department'),
    path('delete-department/<id>', delete_department, name='delete_department'),
    path('employees/', employees, name='employees'),
    path('update-employee/<id>', update_employee, name='update_employee'),
    path('delete-employee/<id>', delete_employee, name='delete_employee'),
]