from django.contrib import admin
from .models import Reserva  # Importa el modelo Reserva

# Registra el modelo Reserva en el admin
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    # Opcional: Personaliza cómo se muestra el modelo en el admin
    list_display = ('id', 'cliente', 'mesa', 'fecha', 'hora')  # Cambia estos campos según los que tengas en el modelo Reserva
    search_fields = ('cliente__nombre', 'mesa__numero')  # Cambia estos campos según los que tengas en el modelo Reserva
    list_filter = ('fecha', 'hora')  # Filtra por estos campos, si están en el modelo Reserva