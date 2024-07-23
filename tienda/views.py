from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from productos.models import Producto
from tienda.forms import CargarForm
# Create your views here.
def cargar_imagen(request):
    params={}

    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)
        params['form']=form 
        if form.is_valid():
            producto = form.cleaned_data['producto']
            precio = form.cleaned_data['precio']
            descripcion = form.cleaned_data['descripcion']
            fecha_publicacion = form.cleaned_data['fecha_publicacion']
            imagen = form.cleaned_data['imagen']
            nuevo_producto = Producto(producto = producto,precio = precio, fecha_publicacion =fecha_publicacion, imagen=imagen)
            nuevo_producto.save()
            return redirect('home')
    else:
        form = CargarForm()
        params['form'] = form
        return render(request, 'tienda/formulario.html', params)
