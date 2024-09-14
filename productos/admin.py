from django.contrib import admin
from productos.models import *

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Relacion", {"fields":["animal", "marca"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'fecha_publicacion','producto','estado','imagen','descripcion'
                ]
            },
        ),
        (
            "Datos economicos",
            {
                "fields": [
                    'precio','stock','descuento'
                ]
            },
        ),    
    ]
    list_display = ['producto', 'fecha_publicacion','estado_de_producto']
    ordering = ['-fecha_publicacion']
    list_filter = ('producto', 'fecha_publicacion',)
    search_fields=('producto', 'estado',)
    list_display_links = ('producto', 'fecha_publicacion',)

    def publicar(self, request, queryset):
        queryset.update(estado="Publicado")
    publicar.short_description = "Pasar a estado Publicado"


admin.site.register(Animal)
admin.site.register(Marca)