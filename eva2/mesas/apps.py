from django.apps import AppConfig

class MesasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Para Django 3.2 o superior
    name = 'mesas'  # Nombre de la aplicación, asegúrate de que coincide con la carpeta de la app
