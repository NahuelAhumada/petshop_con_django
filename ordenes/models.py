from django.db import models

# Create your models here.
from productos.models import Producto
from home.models import Cliente

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
    def __str__(self):
        return self.cliente.nombre + ' - ' + self.id_transaccion

class Orden_Producto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField(default=0, null=True)

    def total(self):
        return self.cantidad*self.producto.precio
    def __str__(self):
        return self.orden.id_transaccion + ' - ' + self.producto.producto