from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email

class Company(models.Model):
    name = models.TextField(max_length=100)
    employees = models.ManyToManyField(CustomUser)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.name
