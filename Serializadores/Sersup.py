from rest_framework import serializers
from Modelosyrutas.Modelosup import Superviviente

class SupervivienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superviviente
        fields = ['id', 'name', 'description', 'usagerate', 'imageUrl'] 
