from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserva_list, name='reserva_list'),              # Lista de todas las reservas
    path('create/', views.reserva_create, name='reserva_create'),    # Crear una nueva reserva
    path('<int:pk>/', views.reserva_detail, name='reserva_detail'),  # Detalle de una reserva específica
    path('<int:pk>/update/', views.reserva_update, name='reserva_update'),  # Actualizar una reserva
    path('<int:pk>/delete/', views.reserva_delete, name='reserva_delete'),  # Eliminar una reserva
]
