from django.urls import path

from ordenes import views

urlpatterns = [
    path('carrito/', views.carrito,name='carrito')
]
