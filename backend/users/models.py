from django.contrib.auth.models import AbstractUser
from django.db import models

from companies.models import Company


class User(AbstractUser):
    class Roles(models.TextChoices):
        OWNER = "OWNER"
        ADMIN = "ADMIN"
        EMPLOYEE = "EMPLOYEE"

    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, related_name='members')
    role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.EMPLOYEE)

    def __str__(self):
        return self.username

