from django.urls import path

from home import views

urlpatterns = [
    path('', views.index),
    path('product/', views.product,name="product"),
    path('carrito/', views.carrito,name="carrito")
]
