from django.db import models 

class Superviviente(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=200)
    description = models.TextField()
    perks = models.JSONField()  
    imageUrl = models.URLField()  
    dlc = models.CharField(max_length=200)

    def __str__(self):
        return self.name
