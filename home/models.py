from django.db import models

# Create your models here.
class Producto(models.Model):
    producto = models.CharField(max_length=200)
    precio= models.DecimalField(max_digits=12,decimal_places=2)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    animal = models.CharField(max_length=20)
    categoria = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)