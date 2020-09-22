from django.db import models

# Create your models here.
class Usuario(models.Model):
    Usuario_nombre = models.CharField(max_length=200)
    Usuario_cedula = models.CharField(max_length=13)
    Usuario_salida = models.DateTimeField("fecha de salida")

    def __str__(self):
        return self.Usuario_nombre

