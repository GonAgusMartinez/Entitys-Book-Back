import json
from django.core.management.base import BaseCommand
from Modelosyrutas.Modelosup import Superviviente  # Asegúrate de que el import esté correcto

class Command(BaseCommand):
    help = 'Cargar datos de supervivientes desde un archivo JSON a la base de datos'

    def handle(self, *args, **kwargs):
        with open('Apidates/Supervivientes.json', 'r', encoding='utf-8') as file:
            supervivientes_data = json.load(file)
            for superviviente in supervivientes_data:
                Superviviente.objects.create(
                    id=superviviente['id'],
                    name=superviviente['name'],
                    description=superviviente['description'],
                    perks=superviviente['perks'],
                    imageUrl=superviviente['imageUrl'],  # Ahora usamos 'imageUrl' como en el JSON
                    dlc=superviviente['dlc']
                )
        self.stdout.write(self.style.SUCCESS('Datos de supervivientes cargados exitosamente'))
