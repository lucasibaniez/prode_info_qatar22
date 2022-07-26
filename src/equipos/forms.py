from dataclasses import fields
from django import forms 

from .models import Equipo

class EquipoForm(forms.ModelForm):
    nombre=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    # cantidad_jugadores=forms.IntegerField()

    class  Meta:
        model = Equipo
        fields = ["nombre"]

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        if nombre[0] != "A":
            raise forms.ValidationError("El nombre del equipo debe iniciar con la letra A")
        return nombre