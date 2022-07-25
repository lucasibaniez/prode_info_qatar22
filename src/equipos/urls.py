from django.urls import path

from . import views

app_name="equipos"

urlpatterns = [
    path("crear/", views.Crear.as_view())
]