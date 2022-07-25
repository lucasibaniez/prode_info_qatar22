from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView

from .forms import EquipoForm
from .models import Equipo

class Crear(LoginRequiredMixin, CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "equipos/crear.html"

    def get_success_url(self, **kwargs):
        return reverse('home')


