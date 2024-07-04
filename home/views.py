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
    productos_orden=Orden_Producto.objects.all()
    params = {'productos_orden':productos_orden}
    return  render(request, 'home/carrito.html', params)