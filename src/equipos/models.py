from distutils.command.upload import upload
from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    
    # Archivo binario
    logo = models.ImageField(upload_to="logo_equipos", null=True, blank=True)

    def __str__(self):
        return self.nombre