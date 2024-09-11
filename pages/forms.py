from django import forms
from .models import Proceso
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulario de modelo para el modelo Proceso
class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['numero', 'nombre', 'descripcion']

# Formulario personalizado para la creación de usuarios
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Formulario de filtro para el modelo Proceso
class ProcesoFilterForm(forms.Form):
    numero = forms.IntegerField(required=False, label='Número')
    nombre = forms.CharField(required=False, max_length=100, label='Nombre')
    descripcion = forms.CharField(required=False, max_length=100, label='Descripción')
