from pyexpat import model
from django import forms 

from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

class UsuarioRegistroForm(UserCreationForm):
    class Meta:
        model=Usuario
        fields=["first_name", "last_name", "username", "password1", "password2"]