from django.shortcuts import render, get_object_or_404, redirect
from .models import Mesa
from .forms import MesaForm  # Asegúrate de tener definido MesaForm en forms.py

# Lista de Mesas
def mesa_list(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas/mesa_list.html', {'mesas': mesas})

# Crear una Nueva Mesa
def mesa_create(request):
    if request.method == 'POST':
        form = MesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mesa_list')
    else:
        form = MesaForm()
    return render(request, 'mesas/mesa_form.html', {'form': form})

# Detalle de una Mesa Específica
def mesa_detail(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    return render(request, 'mesas/mesa_detail.html', {'mesa': mesa})

# Actualizar una Mesa
def mesa_update(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    if request.method == 'POST':
        form = MesaForm(request.POST, instance=mesa)
        if form.is_valid():
            form.save()
            return redirect('mesa_list')
    else:
        form = MesaForm(instance=mesa)
    return render(request, 'mesas/mesa_form.html', {'form': form})

# Eliminar una Mesa
def mesa_delete(request, pk):
    mesa = get_object_or_404(Mesa, pk=pk)
    if request.method == 'POST':
        mesa.delete()
        return redirect('mesa_list')
    return render(request, 'mesas/mesa_delete.html', {'mesa': mesa})
