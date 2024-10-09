from django.db import models

class HabilidadAsesino(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    usagerate = models.CharField(max_length=10)
    imageUrl = models.URLField()

    def __str__(self):
        return self.name