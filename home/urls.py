from django.urls import path

from home import views

urlpatterns = [
    path('', views.index),
    path('producto/', views.Producto,name="producto"),
    path('carrito/', views.carrito,name="carrito")
]
