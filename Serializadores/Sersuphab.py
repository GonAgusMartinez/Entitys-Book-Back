from rest_framework import serializers
from Modelosyrutas.Modelosuphab import HabilidadSuperviviente

class HabilidadeSupervivienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabilidadSuperviviente
        fields = [
            'name',
            'id',
            'description',
            'usagerate',
            'imageUrl'
        ]