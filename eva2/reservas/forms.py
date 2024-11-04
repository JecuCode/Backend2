from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 'mesa', 'fecha', 'hora']  # Ajusta estos campos según los que tengas en el modelo Reserva

        # Opcional: agregar etiquetas o widgets para personalizar la apariencia de los campos
        labels = {
            'cliente': 'Cliente',
            'mesa': 'Mesa',
            'fecha': 'Fecha de Reserva',
            'hora': 'Hora de Reserva',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }
