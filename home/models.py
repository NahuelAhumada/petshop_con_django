from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_de_creacion = models.DateTimeField('Fecha de orden')
    completada = models.BooleanField(default=False, null=True, blank=False)
    id_transaccion = models.CharField(max_length=200, null=True)

    @property
    def precio_total_carrito(self):
        orden_producto = self.orden_producto_set.all()
        total=sum([producto.total() for producto in orden_producto])
        return total
    @property
    def cantidad_total_carrito(self):
        orden_producto = self.orden_producto_set.all()
        total=sum([producto.cantidad for producto in orden_producto])
        return total
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return 's%' % self.nombre
class Producto(models.Model):
    producto = models.CharField(max_length=200)
    precio= models.DecimalField(max_digits=12,decimal_places=2)
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True)

    def __str__(self,):
        return self.producto + " --- " +str(self.fecha_publicacion)
"""     @property
    def url_imagen(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url """
class Orden_Producto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True)

    def total(self):
        return self.cantidad*self.producto.precio

class Envio(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=200)
    def __str__(self):
        return self.direccion
class Marca(models.Model):
    nombre =models.CharField(max_length=200)
    