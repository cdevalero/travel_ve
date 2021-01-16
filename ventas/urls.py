from ventas.views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', index, name="index"),
    path('registrar_nuevo_cliente/', Ventas_registrar_nuevo_cliente, name="Ventas_registrar_nuevo_cliente"),
]
