from django.db import models

class HabilidadSuperviviente(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    usagerate = models.CharField(max_length=10)
    perks = models.JSONField()  # Almacena perks como un JSON array
    imagenUrl = models.URLField()

    def __str__(self):
        return self.name