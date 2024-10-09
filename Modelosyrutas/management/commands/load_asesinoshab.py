from django.core.management.base import BaseCommand
from Modelosyrutas.Modeloasehab import HabilidadAsesino  
import json

class Command(BaseCommand):
    help = 'Carga datos de habilidades de asesinos desde el archivo JSON'

    def handle(self, *args, **kwargs):
        # Especifica la ruta del archivo JSON
        with open('Apidates/Habilidadesase.json', encoding='utf-8') as file:
            data = json.load(file)

            for habilidad in data:
                # Crear una nueva instancia de HabilidadAsesino con los datos del JSON
                HabilidadAsesino.objects.create(
                    name=habilidad['name'],
                    id=habilidad['id'],
                    description=habilidad['description'],
                    usagerate=habilidad['usagerate'],
                    imageUrl=habilidad['imageUrl']
                )

        self.stdout.write(self.style.SUCCESS('Habilidades de asesinos cargadas exitosamente'))
