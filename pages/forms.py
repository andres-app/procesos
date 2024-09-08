from django import forms
from .models import Proceso

class ProcesoForm(forms.ModelForm):
    class Meta:
        model = Proceso
        fields = ['numero', 'nombre', 'descripcion']


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

