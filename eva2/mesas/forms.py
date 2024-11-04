from django import forms
from .models import Mesa

# Formulario para Mesa
class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = ['numero', 'capacidad']  # Asegúrate de que estos nombres coincidan con los campos del modelo Mesa
