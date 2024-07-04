from django.contrib import admin
from home.models import *


admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(Orden_Producto)
admin.site.register(Envio)