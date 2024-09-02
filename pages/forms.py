from django import forms
from .models import Proceso

class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['numero', 'nombre', 'descripcion']
