from django.core.management.base import BaseCommand
from Modelosyrutas.Modelosuphab import HabilidadSuperviviente  
import json

class Command(BaseCommand):
    help = 'Carga datos de habilidades de supervivientes desde el archivo JSON'

    def handle(self, *args, **kwargs):
        # Especifica la ruta del archivo JSON
        with open('Apidates/Habilidadessup.json', encoding='utf-8') as file:
            data = json.load(file)

            for habilidad in data:
                # Crear una nueva instancia de HabilidadSuperviviente con los datos del JSON
                HabilidadSuperviviente.objects.create(
                    name=habilidad['name'],
                    id=habilidad['id'],
                    description=habilidad['description'],
                    usagerate=habilidad['usagerate'],
                    imageUrl=habilidad['imageUrl']
                )

        self.stdout.write(self.style.SUCCESS('Habilidades de supervivientes cargadas exitosamente'))

