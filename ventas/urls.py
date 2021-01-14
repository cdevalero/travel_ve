from ventas.views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', Ventas_base, name="Ventas_base"),
]
