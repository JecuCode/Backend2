from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

# Lista de Reservas
def reserva_list(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas/reserva_list.html', {'reservas': reservas})

# Crear una Nueva Reserva
def reserva_create(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm()
    return render(request, 'reservas/reserva_form.html', {'form': form})

# Detalle de una Reserva Específica
def reserva_detail(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'reservas/reserva_detail.html', {'reserva': reserva})

# Actualizar una Reserva
def reserva_update(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reserva_list')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/reserva_form.html', {'form': form})

# Eliminar una Reserva
def reserva_delete(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reserva_list')
    return render(request, 'reservas/reserva_delete.html', {'reserva': reserva})
