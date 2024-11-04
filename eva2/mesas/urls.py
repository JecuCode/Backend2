from django.urls import path
from . import views

urlpatterns = [
    path('', views.mesa_list, name='mesa_list'),                  # Ruta para listar todas las mesas
    path('create/', views.mesa_create, name='mesa_create'),       # Ruta para crear una nueva mesa
    path('<int:pk>/', views.mesa_detail, name='mesa_detail'),     # Ruta para ver detalles de una mesa específica
    path('<int:pk>/update/', views.mesa_update, name='mesa_update'), # Ruta para actualizar una mesa específica
    path('<int:pk>/delete/', views.mesa_delete, name='mesa_delete'), # Ruta para eliminar una mesa específica
]
