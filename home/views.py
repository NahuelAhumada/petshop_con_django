from django.shortcuts import render
from home.models import *
from django.db.models import Q
# Create your views here.
def index(request):
    productos = Producto.objects.all()
    params = {}
    params['nombre_sitio'] = "Vida Silvestre"
    params['productos'] = productos
    return render(request, 'home/index.html', params)
def product(request):
    params = {}
    return  render(request, 'home/producto.html', params)
def carrito(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente
        orden, orden_creada = Orden.objects.get_or_create(cliente=cliente, completada=False)
        productos_orden = orden.orden_producto_set.all()
    else:
        productos_orden = []
        orden={'precio_total_carrito':0, 'cantidad_total_carrito':0}
    params = {'productos_orden':productos_orden, 'orden':orden}
    return  render(request, 'home/carrito.html', params)