from django.shortcuts import render
from django.views.generic import TemplateView

from equipos.models import Equipo


def inicio(request):
    template_name="inicio.html"
    
    ctx={}
    return render(request, template_name, ctx)

"""
def login(request):
    return render(request, "login.html", {})


Vista basada en funcion
def mis_grupos(request):
    return render(request, "mis_grupos.html", {})

"""    

class MisGrupos(TemplateView):
    template_name = "mis_grupos.html"