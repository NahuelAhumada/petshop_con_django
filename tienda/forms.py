from django.forms import ModelForm
from productos.models import Producto

class CargarForm(ModelForm):
    class Meta:
        model=Producto
        fields=['producto','precio','descripcion','fecha_publicacion','imagen']
    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__( *args, **kwargs)