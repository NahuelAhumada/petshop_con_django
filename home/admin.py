from django.contrib import admin
from home.models import Producto 
from home.models import Categoria

class ProductoAdmin(admin.ModelAdmin):
    fields= ['fecha_publicacion','producto','imagen']

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
#admin.site.register(Producto)