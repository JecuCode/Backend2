from django.db import models

class Cliente(models.Model):
    # Define los campos del modelo Cliente
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Asegura que el email sea único
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)  # Se agrega la fecha automáticamente

    def __str__(self):
        return self.nombre  # Muestra el nombre como representación del cliente en la base de datos

    class Meta:
        ordering = ['nombre']  # Ordena los clientes alfabéticamente
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
