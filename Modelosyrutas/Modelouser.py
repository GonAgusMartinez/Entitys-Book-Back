from django.db import models

class Usuario(models.Model):
    ADMIN = 'admin'
    USER = 'user'
    USER_TYPE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    imagen = models.URLField(max_length=200, blank=True, null=True)
    ban_status = models.BooleanField(default=False)
    comentaries = models.CharField(max_length=2000, blank=True, null=True)  
    usertype = models.CharField(max_length=200, choices=USER_TYPE_CHOICES, default=USER)  

    def __str__(self):
        return self.username
