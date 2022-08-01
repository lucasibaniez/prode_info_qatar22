from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView

from .forms import EquipoForm
from .models import Equipo

class Crear(LoginRequiredMixin, CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = "equipos/crear.html"

    def get_success_url(self, **kwargs):
        return reverse('equipos:listar')
    
         

class Listar(LoginRequiredMixin, ListView):
    template_name="equipos/listar.html"
    model=Equipo        
    context_object_name = "equipos"
    paginate_by=2

    def get_queryset(self):
        return Equipo.objects.all().order_by("id")

class Actualizar(LoginRequiredMixin, UpdateView):
    template_name="equipos/actualizar.html"
    model=Equipo
    form_class = EquipoForm

    def get_success_url(self, **kwargs):
        return reverse('equipos:listar')