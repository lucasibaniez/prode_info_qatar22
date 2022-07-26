from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import UsuarioRegistroForm
from .models import Usuario

class Registro(CreateView):
    model = Usuario
    form_class = UsuarioRegistroForm
    template_name = "usuarios/registro.html"

    def get_success_url(self, **kwargs):
        return reverse('home')