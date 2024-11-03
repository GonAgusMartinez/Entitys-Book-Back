from django.core.management.base import BaseCommand
from Modelosyrutas.Modelosup import Superviviente
import json

class Command(BaseCommand):
    help = 'Cargar datos de supervivientes desde un archivo JSON a la base de datos'

    def handle(self, *args, **kwargs):
        with open('Apidates/Supervivientes.json', 'r', encoding='utf-8') as file:
            supervivientes_data = json.load(file)
            for superviviente in supervivientes_data:
                Superviviente.objects.update_or_create(
                    id=superviviente['id'],
                    defaults={
                        'name': superviviente['name'],
                        'description': superviviente['description'],
                        'usagerate': superviviente['usagerate'],
                        'imageUrl': superviviente['imageUrl'],
                    }
                )
        self.stdout.write(self.style.SUCCESS('Datos de supervivientes actualizados exitosamente'))
