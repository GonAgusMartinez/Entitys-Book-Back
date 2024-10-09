from rest_framework import serializers
from Modelosyrutas.Modeloasehab import HabilidadAsesino

class HabilidadAsesinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabilidadAsesino
        fields = ['name', 'description', 'usagerate', 'imageUrl']