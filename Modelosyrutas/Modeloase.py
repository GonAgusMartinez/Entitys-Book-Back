from django.db import models

class Asesino(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    usagerate = models.CharField(max_length=10)
    killrate_onekill = models.IntegerField()
    killrate_twokills = models.IntegerField()
    killrate_threekills = models.IntegerField()
    killrate_fourkills = models.IntegerField()
    perks = models.JSONField()  # Guardaremos las perks como un JSON array
    imagenUrl = models.URLField()
    power = models.CharField(max_length=100)
    powerdescription = models.TextField()
    speedmove = models.CharField(max_length=10)
    high = models.CharField(max_length=50)
    terrorradio = models.CharField(max_length=10)
    dlc = models.CharField(max_length=100)

    def __str__(self):
        return self.name