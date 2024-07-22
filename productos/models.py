from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre =models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
class Animal(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return self.nombre
class Producto(models.Model):
    producto = models.CharField(max_length=200)
    precio= models.DecimalField(max_digits=12,decimal_places=2)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True)
    animal = models.ForeignKey(Animal, blank=True, null=True, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self,):
        return self.producto + " --- " +str(self.fecha_publicacion)
""" @property
    def url_imagen(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url """