from http.client import HTTPResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from usuarios.models import Usuario

from .forms import GrupoForm
from .models import Grupo, GrupoUsuarios


class Listar(LoginRequiredMixin, ListView):
    template_name="grupos/listar.html"
    model=Grupo        
    context_object_name = "grupos"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        # context["dato"] = "esto es un dato"
        return context

    def get_queryset(self):
        return self.request.user.mis_grupos.all() # Grupo.objects.filter(creador=self.request.user)

class Crear(LoginRequiredMixin, CreateView):
    model = Grupo
    form_class = GrupoForm
    template_name = "grupos/crear.html"

    def form_valid(self, form):
        f = form.save(commit=False)
        f.creador_id=self.request.user.id
        return super(Crear, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('grupos:listar')
    
    def get_form_kwargs(self):
        kwargs=super(Crear, self).get_form_kwargs()  
        kwargs["usuario_id"]=self.request.user.id
        return kwargs

def ver(request, pk):
    template_name="grupos/ver.html"
    ctx={
        "grupo": Grupo.objects.get(id=pk)
    }
    return render(request, template_name, ctx) 


def inscripciones(request, id_grupo, id_usuario):
    gu=GrupoUsuarios.objects.create(
        grupo=Grupo.objects.get(id=id_grupo),
        usuario=Usuario.objects.get(id=id_usuario)  
    )
    return HttpResponseRedirect(reverse('grupos:listar'))
