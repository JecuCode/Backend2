# admin.py en la aplicación correspondiente
from django.contrib import admin
from .models import Mesa

# Registrar el modelo Mesa en el panel de administración
admin.site.register(Mesa)
