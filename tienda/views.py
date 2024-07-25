from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from productos.models import Producto
from tienda.forms import CargarForm
from django.http import Http404
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
    
class VerImagenes(View):
    template = "tienda/verproductos.html"

    def get(self, request):
        params={}
        try: 
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"]=productos

        return render(request, self.template,params)

def ver_imagen(request, producto_id):
    params={}
    try: 
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"]=producto
    return render(request, "tienda/verproducto.html",params)
