from django.contrib import admin
from django.urls import path
from Modelosyrutas.views import (
    AsesinoList, 
    AsesinoDetail, 
    SupervivienteList, 
    SupervivienteDetail, 
    HabilidadAsesinoList, 
    HabilidadAsesinoDetail, 
    HabilidadSupervivienteList, 
    HabilidadSupervivienteDetail  # Importa las vistas para habilidades de supervivientes
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas para asesinos
    path('api/asesinos/', AsesinoList.as_view(), name='asesinos-list'),
    path('api/asesinos/<int:pk>/', AsesinoDetail.as_view(), name='asesinos-detail'),
    
    # Rutas para supervivientes
    path('api/supervivientes/', SupervivienteList.as_view(), name='supervivientes-list'),
    path('api/supervivientes/<int:pk>/', SupervivienteDetail.as_view(), name='supervivientes-detail'),
    
    # Rutas para habilidades de asesinos
    path('api/habilidades_asesinos/', HabilidadAsesinoList.as_view(), name='habilidades-asesinos-list'),
    path('api/habilidades_asesinos/<int:pk>/', HabilidadAsesinoDetail.as_view(), name='habilidades-asesinos-detail'),
    
    # Rutas para habilidades de supervivientes
    path('api/habilidades_supervivientes/', HabilidadSupervivienteList.as_view(), name='habilidades-supervivientes-list'),
    path('api/habilidades_supervivientes/<int:pk>/', HabilidadSupervivienteDetail.as_view(), name='habilidades-supervivientes-detail'),
]