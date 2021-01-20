from ventas.views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', index, name="index"),
    path('registrar_nuevo_cliente/', Ventas_registrar_nuevo_cliente, name="Ventas_registrar_nuevo_cliente"),
    path('Ventas_intrumento_1/', Ventas_intrumento_1, name="Ventas_intrumento_1"),
    path('Ventas_intrumento_2/', Ventas_intrumento_2, name="Ventas_intrumento_2"),

    path('Ventas_crear_nuevo_viajero/', Ventas_crear_nuevo_viajero, name="Ventas_crear_nuevo_viajero"),
]
