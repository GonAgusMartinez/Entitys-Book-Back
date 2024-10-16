from rest_framework import serializers
from Modelosyrutas.Modelosuphab import HabilidadSuperviviente

class HabilidadeSupervivienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabilidadSuperviviente
        fields = [
            'id',  # Aseguramos que el ID esté presente
            'name',
            'description',
            'usagerate',
            'imageUrl'
        ]