from rest_framework import serializers
from Modelosyrutas.Modelosuphab import Habilidadesuperviviente

class HabilidadeSupervivienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidadesuperviviente
        fields = [
            'name',
            'id',
            'description',
            'usagerate',
            'imageUrl'
        ]