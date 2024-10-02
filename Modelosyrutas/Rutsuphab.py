from django.urls import path
from .views import HabilidadSupervivienteList, HabilidadSupervivienteDetail

urlpatterns = [
    path('habilidades_supervivientes/', HabilidadSupervivienteList.as_view(), name='habilidades-supervivientes-list'),
    path('habilidades_supervivientes/<int:id>/', HabilidadSupervivienteDetail.as_view(), name='habilidades-supervivientes-detail'),
]