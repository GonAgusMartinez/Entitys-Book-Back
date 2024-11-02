from rest_framework import serializers
from Modelosyrutas.Modelouser import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'