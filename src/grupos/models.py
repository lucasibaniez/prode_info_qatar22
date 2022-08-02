from django.db import models

from usuarios.models import Usuario

class Grupo(models.Model):
    nombre=models.CharField(max_length=255)
    creador=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mis_grupos")

    participantes = models.ManyToManyField(Usuario) # OneToOne

    portada = models.ImageField(upload_to="portadas_grupos", null=True, blank=True)

    class Meta:
        db_table = "grupos"

"""
class GrupoUsuarios(models.Model):
    grupo=models.ForeignKey(Grupo, on_delete=models.CASCADE)
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
"""