from django.shortcuts import render


from equipos.models import Equipo


def inicio(request):
    template_name="inicio.html"

    equipos = Equipo.objects.all()

    ctx={
        'equipos': equipos,
        'nombre': "Octavio"
    }
    return render(request, template_name, ctx)

def login(request):
    return render(request, "login.html", {})