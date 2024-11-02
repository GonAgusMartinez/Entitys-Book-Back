from django.contrib import admin
from Modelosyrutas.Modeloase import Asesino
from Modelosyrutas.Modeloasehab import HabilidadAsesino
from Modelosyrutas.Modelosup import Superviviente
from Modelosyrutas.Modelosuphab import HabilidadSuperviviente
from Modelosyrutas.Modelouser import Usuario  # Importa el modelo de usuario

admin.site.register(Asesino)
admin.site.register(HabilidadAsesino)
admin.site.register(Superviviente)
admin.site.register(HabilidadSuperviviente)
admin.site.register(Usuario)  # Registra el modelo de usuario