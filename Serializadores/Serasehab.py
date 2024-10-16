from rest_framework import serializers
from Modelosyrutas.Modeloasehab import HabilidadAsesino

class HabilidadAsesinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabilidadAsesino
        fields = ['id', 'name', 'description', 'usagerate', 'imageUrl']  # Incluye el campo id