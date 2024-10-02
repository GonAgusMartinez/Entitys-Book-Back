class Habilidadase(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    usagerate = models.CharField(max_length=10)
    imagenUrl = models.URLField()
    type = models.CharField(max_length=10)  # 'killer' o 'survivor'

    def __str__(self):
        return self.name