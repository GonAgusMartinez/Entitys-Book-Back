from django.db import models

class HabilidadSuperviviente(models.Model):
    id = models.IntegerField(primary_key=True)  # Asegúrate de que el campo ID esté definido
    name = models.CharField(max_length=100)
    description = models.TextField()
    usagerate = models.CharField(max_length=10)
    imageUrl = models.URLField()  # Este es el campo que necesita estar presente para evitar el error

    def __str__(self):
        return self.name