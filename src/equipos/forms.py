from dataclasses import fields
from django import forms 

from .models import Equipo

class EquipoForm(forms.ModelForm):
    class  Meta:
        model = Equipo
        fields = ["nombre"] 