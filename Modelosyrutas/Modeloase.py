from django.db import models

class Asesino(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=200)
    description = models.TextField()
    usagerate = models.CharField(max_length=200)
    killrate_onekill = models.IntegerField()
    killrate_twokills = models.IntegerField()
    killrate_threekills = models.IntegerField()
    killrate_fourkills = models.IntegerField()
    perks = models.JSONField() 
    imagenUrl = models.URLField()
    power = models.CharField(max_length=200)
    powerdescription = models.TextField()
    speedmove = models.CharField(max_length=200)
    high = models.CharField(max_length=200)
    terrorradio = models.CharField(max_length=200)
    dlc = models.CharField(max_length=200)

    def __str__(self):
        return self.name