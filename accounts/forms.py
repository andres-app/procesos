# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser  # Importa tu modelo de usuario personalizado

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Asegúrate de que este sea tu modelo personalizado
        fields = ('username', 'email', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser  # Asegúrate de que este sea tu modelo personalizado
        fields = ('username', 'email')  # Puedes añadir más campos si es necesario
