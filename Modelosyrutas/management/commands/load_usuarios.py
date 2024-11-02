from django.core.management.base import BaseCommand
from Modelosyrutas.Modelouser import Usuario  # Modelo de usuarios
import json

class Command(BaseCommand):
    help = 'Cargar datos de usuarios desde un archivo JSON a la base de datos'

    def handle(self, *args, **kwargs):
        with open('Apidates/Usuarios.json', 'r', encoding='utf-8') as file:
            usuarios_data = json.load(file)
            for usuario in usuarios_data:
                Usuario.objects.create(
                    id=usuario['id'],
                    username=usuario['username'],
                    email=usuario['email'],
                    imagen=usuario['imagen'],
                    ban_status=usuario['ban_status'],
                    comentaries=usuario['comentaries'],
                    usertype=usuario['usertype']
                )
        self.stdout.write(self.style.SUCCESS('Datos de usuarios cargados exitosamente'))
