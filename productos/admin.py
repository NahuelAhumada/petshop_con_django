from django.contrib import admin
from productos.models import *
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

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
    actions=["publicar", "exportar_a_json", "ver_productos"]

    def publicar(self, request, queryset):
        registro=queryset.update(estado="Publicado")
        if registro == 1:
            mensaje = "1 registro actualizado"
        else:
            mensaje = "%s registros actualizados" % registro
        self.message_user(request, "%s exitosamente" % mensaje)
    publicar.short_description = "Pasar a estado Publicado"

    def exportar_a_json(self,request,queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json",queryset,stream=response)
        return response
    def ver_productos(self, request, queryset):
        params={}
        productos=Producto.objects.all
        params["productos"]=productos
        return render(request, "admin/productos/productos.html",params)
    ver_productos.short_description = "Ver productos"

admin.site.register(Animal)
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    ordering = ['nombre']
