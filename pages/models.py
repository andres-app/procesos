from django.db import models

class Proceso(models.Model):
    numero = models.IntegerField(unique=True)  # Corresponde a la columna 'Nº' en el Excel
    nombre = models.CharField(max_length=100)  # Otro campo de ejemplo
    descripcion = models.TextField()  # Campo de descripción
    creado_en = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    def __str__(self):
        return f"{self.numero} - {self.nombre}"


class Evento(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, related_name='eventos')  # Relación con Proceso
    actividad = models.CharField(max_length=100)  # Campo de texto corto
    documento = models.CharField(max_length=100)  # Campo de texto corto
    fecha = models.DateField()  # Campo de tipo fecha
    situacion = models.TextField()  # Campo de texto largo
    importe = models.DecimalField(max_digits=10, decimal_places=2)  # Campo numérico con 2 decimales

    def __str__(self):
        return f"{self.actividad} - {self.proceso.nombre}"

