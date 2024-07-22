from django.urls import path

from ordenes import views

urlpatterns = [
    path('', views.carrito,name='carrito')
]
