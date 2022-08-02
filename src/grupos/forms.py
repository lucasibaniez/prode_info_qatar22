from django import forms 

from usuarios.models import Usuario

from .models import Grupo

class GrupoForm(forms.ModelForm):

    class  Meta:
        model = Grupo
        fields = ["nombre", "participantes", "portada"]
    
    def __init__(self, usuario_id, *args, **kwargs):
        super(GrupoForm, self).__init__(*args, **kwargs)
        self.fields["participantes"].queryset=Usuario.objects.all().exclude(id=usuario_id)