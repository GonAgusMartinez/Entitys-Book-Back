from rest_framework import generics
from Modelosyrutas.Modeloase import Asesino  # Modelo de asesinos
from Modelosyrutas.Modelosup import Superviviente  # Modelo de supervivientes
from Modelosyrutas.Modeloasehab import HabilidadAsesino  # Modelo de habilidades de asesinos
from Modelosyrutas.Modelosuphab import HabilidadSuperviviente  # Modelo de habilidades de supervivientes
from Serializadores.Serase import AsesinoSerializer  # Serializador de asesinos
from Serializadores.Sersup import SupervivienteSerializer  # Serializador de supervivientes
from Serializadores.Serasehab import HabilidadAsesinoSerializer  # Serializador de habilidades de asesinos
from Serializadores.Sersuphab import HabilidadeSupervivienteSerializer  # Serializador de habilidades de supervivientes

# Vistas para Asesino
class AsesinoList(generics.ListCreateAPIView):
    queryset = Asesino.objects.all()
    serializer_class = AsesinoSerializer

class AsesinoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asesino.objects.all()
    serializer_class = AsesinoSerializer

# Vistas para Superviviente
class SupervivienteList(generics.ListCreateAPIView):
    queryset = Superviviente.objects.all()
    serializer_class = SupervivienteSerializer

class SupervivienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Superviviente.objects.all()
    serializer_class = SupervivienteSerializer

# Vistas para Habilidad de Asesino
class HabilidadAsesinoList(generics.ListCreateAPIView):
    queryset = HabilidadAsesino.objects.all()
    serializer_class = HabilidadAsesinoSerializer

class HabilidadAsesinoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HabilidadAsesino.objects.all()
    serializer_class = HabilidadAsesinoSerializer

# Vistas para Habilidad de Superviviente
class HabilidadSupervivienteList(generics.ListCreateAPIView):
    queryset = HabilidadSuperviviente.objects.all()
    serializer_class = HabilidadeSupervivienteSerializer

class HabilidadSupervivienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HabilidadSuperviviente.objects.all()
    serializer_class = HabilidadeSupervivienteSerializer