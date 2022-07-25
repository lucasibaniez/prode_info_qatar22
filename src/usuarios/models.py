from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    telefono=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
