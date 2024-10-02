from rest_framework import serializers
from Modelosyrutas.Modelosup import Superviviente

class SupervivienteSerializer(serializers.ModelSerializer):
    perks = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Superviviente
        fields = [
            'name',
            'id',
            'description',
            'perks',
            'imageUrl',
            'dlc'
        ]