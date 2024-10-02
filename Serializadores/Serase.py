from rest_framework import serializers
from Modelosyrutas.Modeloase import Asesino 

# Serializador para el campo Killrate
class KillRateSerializer(serializers.Serializer):
    onekill = serializers.IntegerField()
    twokills = serializers.IntegerField()
    threekills = serializers.IntegerField()
    fourkills = serializers.IntegerField()

# Serializador para el modelo Asesino
class AsesinoSerializer(serializers.ModelSerializer):
    # Serializamos el campo anidado 'killrate' con otro serializador
    killrate = KillRateSerializer()

    class Meta:
        model = Asesino
        fields = [
            'name', 
            'id', 
            'usagerate', 
            'description', 
            'perks', 
            'killrate', 
            'imagenUrl', 
            'power', 
            'powerdescription', 
            'speedmove', 
            'high', 
            'terrorradio', 
            'dlc'
        ]