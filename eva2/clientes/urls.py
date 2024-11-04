from django.urls import path
from . import views  # Importa las vistas de la aplicación clientes

urlpatterns = [
    # Lista de clientes
    path('', views.cliente_list, name='cliente_list'),
    
    # Crear un nuevo cliente
    path('create/', views.cliente_create, name='cliente_create'),
    
    # Detalle de un cliente específico
    path('<int:pk>/', views.cliente_detail, name='cliente_detail'),
    
    # Actualizar un cliente
    path('<int:pk>/update/', views.cliente_update, name='cliente_update'),
    
    # Eliminar un cliente
    path('<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
]
