from django.db import models

class Proceso(models.Model):
    numero = models.IntegerField(unique=True)  # Corresponde a la columna 'Nº' en el Excel
    nombre = models.CharField(max_length=100)  # Otro campo de ejemplo
    descripcion = models.TextField()  # Campo de descripción
    creado_en = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    def __str__(self):
        return f"{self.numero} - {self.nombre}"
