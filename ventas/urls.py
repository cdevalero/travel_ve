from ventas.views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', index, name="index"),
    path('Buscar_Paquete/', Buscar_Paquete, name="Buscar_Paquete"),
]
