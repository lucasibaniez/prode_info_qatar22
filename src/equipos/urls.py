from django.urls import path

from . import views

app_name="equipos"

urlpatterns = [
    path("crear/", views.Crear.as_view(), name="crear"),
    path("listar/", views.Listar.as_view(), name="listar"),
]