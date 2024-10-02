from django.urls import path
from .views import HabilidadAsesinoList, HabilidadAsesinoDetail

urlpatterns = [
    path('habilidades_asesinos/', HabilidadAsesinoList.as_view(), name='habilidades-asesinos-list'),
    path('habilidades_asesinos/<int:id>/', HabilidadAsesinoDetail.as_view(), name='habilidades-asesinos-detail'),
]