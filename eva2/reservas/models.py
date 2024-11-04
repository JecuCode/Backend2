from django.db import models
from clientes.models import Cliente  # Asegúrate de que la app clientes esté en INSTALLED_APPS y de importar correctamente
from mesas.models import Mesa        # Asegúrate de que la app mesas esté en INSTALLED_APPS y de importar correctamente

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'Reserva de {self.cliente} para la mesa {self.mesa} el {self.fecha} a las {self.hora}'
