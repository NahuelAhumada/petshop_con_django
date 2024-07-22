from django.shortcuts import render
from ordenes.models import *
# Create your views here.
def carrito(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden, orden_creada = Orden.objects.get_or_create(cliente=cliente, completada=False)
        productos_orden = orden.orden_producto_set.all()
    else:
        productos_orden = []
        orden={'precio_total_carrito':0, 'cantidad_total_carrito':0}
    params = {'productos_orden':productos_orden, 'orden':orden}
    return  render(request, 'ordenes/carrito.html', params)