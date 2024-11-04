from django.db import models

class Mesa(models.Model):
    numero = models.IntegerField(unique=True)  # Número único para identificar la mesa
    capacidad = models.IntegerField()  # Capacidad de personas para cada mesa

    def __str__(self):
        return f"Mesa {self.numero} - Capacidad: {self.capacidad}"
