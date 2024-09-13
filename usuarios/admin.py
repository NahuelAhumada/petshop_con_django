from django.contrib import admin
from usuarios.models import Cliente
# Register your models here.
class Clienteadmin(admin.ModelAdmin):
    list_display = ["usuario", "nombre", "email","clave"]

admin.site.register(Cliente,Clienteadmin)