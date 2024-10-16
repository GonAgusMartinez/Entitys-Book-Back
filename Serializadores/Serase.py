from rest_framework import serializers
from Modelosyrutas.Modeloase import Asesino

# Serializador para el campo Killrate
class KillRateSerializer(serializers.Serializer):
    killrate_onekill = serializers.IntegerField()
    killrate_twokills = serializers.IntegerField()
    killrate_threekills = serializers.IntegerField()
    killrate_fourkills = serializers.IntegerField()

# Serializador para el modelo Asesino
class AsesinoSerializer(serializers.ModelSerializer):
    # Creamos un campo adicional 'killrate' usando el serializador anidado
    killrate = KillRateSerializer(source='*', read_only=True)

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

    def to_representation(self, instance):
        """Sobrescribe el método para crear el campo 'killrate' a partir de los campos individuales."""
        representation = super().to_representation(instance)
        
        # Creamos el campo 'killrate' a partir de los cuatro campos individuales
        representation['killrate'] = {
            'killrate_onekill': instance.killrate_onekill,
            'killrate_twokills': instance.killrate_twokills,
            'killrate_threekills': instance.killrate_threekills,
            'killrate_fourkills': instance.killrate_fourkills
        }
        
        return representation