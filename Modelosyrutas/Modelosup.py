from django.db import models

class Superviviente(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    usagerate = models.CharField(max_length=200, null=True, blank=True)  # Nueva propiedad
    imageUrl = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
