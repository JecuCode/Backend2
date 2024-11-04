from django.contrib import admin
from .models import Cliente  # Importa el modelo Cliente

# Registra el modelo Cliente en el sitio de administración
admin.site.register(Cliente)
