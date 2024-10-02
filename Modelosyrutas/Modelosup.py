class Superviviente(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    perks = models.JSONField()  
    imagenUrl = models.URLField()
    dlc = models.CharField(max_length=100)

    def __str__(self):
        return self.name