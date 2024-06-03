from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return 's%' % self.nombre
class Producto(models.Model):
    producto = models.CharField(max_length=200)
    precio= models.DecimalField(max_digits=12,decimal_places=2)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    animal = models.CharField(max_length=20)
    categoria = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True)

    def __str__(self,):
        return self.producto + " --- " +str(self.fecha_publicacion)