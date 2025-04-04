from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Employee(AbstractUser):
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.username
