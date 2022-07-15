from re import template
from django.shortcuts import render


def inicio(request):
    template_name="inicio.html"
    usuario={
        "nombre": "Lucas",
        "apellido": "Ibañez"
    }
    ctx={
        "user_dict": usuario
    }
    return render(request, template_name, ctx)