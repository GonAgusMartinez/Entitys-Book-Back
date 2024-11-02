from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import generics
from Modelosyrutas.Modelouser import Usuario
from Serializadores.Seruseru import UsuarioSerializer

# Vista para listar todos los usuarios o crear uno nuevo
class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vista para obtener, actualizar o eliminar un usuario específico
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Definición de las rutas
urlpatterns = [
    path('usuarios/', UsuarioList.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioDetail.as_view(), name='usuario-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
