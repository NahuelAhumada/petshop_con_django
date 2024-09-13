from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,null=False, blank=False)
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    clave = models.CharField(max_length=50, blank=True, null=True, default="---")
    
    def __str__(self):
        return self.nombre

