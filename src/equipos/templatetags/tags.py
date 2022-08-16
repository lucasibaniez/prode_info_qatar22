from django import template

register = template.Library()

from equipos.models import Equipo

@register.simple_tag
def mostrar_saludo():
    return "Hola soy un tag"


@register.simple_tag
def saludar(nombre):
    return f"Hola {nombre}"


@register.simple_tag
def get_equipos():
    return Equipo.objects.all()

def nombre_default(parametro1, parametro2):
    if parametro1:
        return parametro1
    return parametro2  
register.filter("nombre_default", nombre_default)