from email.policy import default
from random import choices
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(null=True, blank=True, max_length=30)
    phone_number = PhoneNumberField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.email

class Department(models.Model):
    name = models.CharField(unique=True, null=False, blank=False, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.name


STATUS_CHOICES = (
    ("Active", "Active"),
    ("Inactive", "Inactive")
)

class Initial(models.Model):
    name = models.CharField(unique=True, null=False, blank=False, max_length=5)
    status = models.CharField(choices=STATUS_CHOICES, default="Inactive", max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    initial = models.ForeignKey(Initial, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False, max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField(null=False, blank=False)
    address = models.CharField(null=False, blank=False, max_length=80)
    doj = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-doj']

    def __str__(self) -> str:
        return self.name