from django.core.management.base import BaseCommand
from Modelosyrutas.Modeloase import Asesino  
import json

class Command(BaseCommand):
    help = 'Cargar datos de asesinos desde un archivo JSON a la base de datos'

    def handle(self, *args, **kwargs):
        with open('Apidates/Asesinos.json', 'r', encoding='utf-8') as file:
            asesinos_data = json.load(file)
            for asesino in asesinos_data:
                Asesino.objects.create(
                    id=asesino['id'],  # Añadimos el campo id
                    name=asesino['name'],
                    description=asesino['description'],
                    usagerate=asesino['usagerate'],
                    killrate_onekill=asesino['killrate']['onekill'],
                    killrate_twokills=asesino['killrate']['twokills'],
                    killrate_threekills=asesino['killrate']['threekills'],
                    killrate_fourkills=asesino['killrate']['fourkills'],
                    perks=asesino['perks'],
                    imagenUrl=asesino['imagenUrl'],
                    power=asesino['power'],
                    powerdescription=asesino['powerdescription'],
                    speedmove=asesino['speedmove'],
                    high=asesino['high'],
                    terrorradio=asesino['terrorradio'],
                    dlc=asesino['dlc']
                )
        self.stdout.write(self.style.SUCCESS('Datos de asesinos cargados exitosamente'))