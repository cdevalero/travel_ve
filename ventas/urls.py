from ventas.views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', index, name="index"),
    path('Buscar_Paquete/', Buscar_Paquete, name="Buscar_Paquete"),
    path('ver_mas_paquete/<id>', ver_mas_paquete, name="ver_mas_paquete"),
    path('seleccionar_asesor/', seleccionar_asesor, name="seleccionar_asesor"),
    path('ventas_buscar_paquete/<agente>/<cliente>', ventas_buscar_paquete, name="ventas_buscar_paquete"),
    path('ventas_ver_mas_paquete/<id>/<agente>/<cliente>', ventas_ver_mas_paquete, name="ventas_ver_mas_paquete"),
    path('ventas_comprar_paquete/<paquete>/<agente>/<cliente>/<precio>/<fecha>/<agencia>', ventas_comprar_paquete, name="ventas_comprar_paquete"),
    path('ventas_presupuesto/<paquete>/<agente>/<cliente>/<precio>/<fecha>/<agencia>', ventas_presupuesto, name="ventas_presupuesto"),
    path('ventas_intrumento/<cliente>/<contrato>/<tipo>/<descuento>', ventas_intrumento, name="ventas_intrumento"),
    path('ventas_ver_presupuesto/<id_contrato>/<tipo>/<descuento>', ventas_ver_presupuesto, name="ventas_ver_presupuesto"),
    path('confirmar_presupuesto/<contrato>/<numero>/<tipo>/<descuento>', confirmar_presupuesto, name="confirmar_presupuesto"),
    path('ventas_registrar_viajeros/<contrato>/<cuenta>/<numero>/<tipo>/<descuento>', ventas_registrar_viajeros, name="ventas_registrar_viajeros"),
    path('ventas_registrar_viajeros_terminar/<contrato>/<cuenta>/<numero>/<tipo>/<descuento>', ventas_registrar_viajeros_terminar, name="ventas_registrar_viajeros_terminar"),
    path('ver_contrato/<id_contrato>/<numero>/<tipo>/<descuento>', ver_contrato, name="ver_contrato"),
]
