from rest_framework import serializers
from Modelosyrutas.Modeloasehab import Habilidadeasesino

class HabilidadeAsesinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidadeasesino
        fields = [
            'name',
            'id',
            'description',
            'usagerate',
            'imageUrl'
        ]