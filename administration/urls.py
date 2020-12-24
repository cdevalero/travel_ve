from django.contrib import admin
from django.urls import path, include
from .views import *


'''
    TEST
    path('', Test_Show, name="Test_Show"),
    path('Test_ShowDepartamentos/', Test_ShowDepartamentos, name="Test_ShowDepartamentos"),
    path('Test_ShowEmpleados/', Test_ShowEmpleados, name="Test_ShowEmpleados"),
'''

urlpatterns = [

    # SHOW
    path('Show_bancos/', Show_bancos, name="Show_bancos"),
    path('Show_Clientes/', Show_Clientes, name="Show_Clientes"),
    path('Show_Areas_de_interes/', Show_Areas_de_interes, name="Show_Areas_de_interes"),
    path('Show_paises/', Show_paises, name="Show_paises"),
    path('Show_rallies/', Show_rallies, name="Show_rallies"),
    path('Show_premios/', Show_premios, name="Show_premios"),
    path('Show_Ciudades/', Show_Ciudades, name="Show_Ciudades"),
    path('Show_Atracciones/', Show_Atracciones, name="Show_Atracciones"),
    path('Show_Circuitos/', Show_Circuitos, name="Show_Circuitos"),
    path('Show_atr_cir/', Show_atr_cir, name="Show_atr_cir"),
    path('Show_Registro_clientes/', Show_Registro_clientes, name="Show_Registro_clientes"),
    path('Show_Alojamientos/', Show_Alojamientos, name="Show_Alojamientos"),
    path('Show_Proveedores/', Show_Proveedores, name="Show_Proveedores"),
    path('Show_pro_age/', Show_pro_age, name="Show_pro_age"),
    path('Show_Asesores_de_viajes/', Show_Asesores_de_viajes, name="Show_Asesores_de_viajes"),
    path('Show_Paquetes/', Show_Paquetes, name="Show_Paquetes"),
    path('Show_Especializaciones/', Show_Especializaciones, name="Show_Especializaciones"),
    path('Show_Clientes/', Show_Precios_paquetes, name="Show_Precios_paquetes"),
    path('Show_Precios_paquetes/', Show_Areas_de_interes, name="Show_Areas_de_interes"),
    path('Show_Calendarios_anuales/', Show_Calendarios_anuales, name="Show_Calendarios_anuales"),
    path('Show_Descuentos/', Show_Descuentos, name="Show_Descuentos"),
    path('Show_Intinerarios/', Show_Intinerarios, name="Show_Intinerarios"),
    path('Show_ITN_ATR/', Show_ITN_ATR, name="Show_ITN_ATR"),
    path('Show_Detalles_servicios/', Show_Detalles_servicios, name="Show_Detalles_servicios"),
    path('Show_ALO_DET/', Show_ALO_DET, name="Show_ALO_DET"),
    path('Show_Instrumentos_de_pago/', Show_Instrumentos_de_pago, name="Show_Instrumentos_de_pago"),
    path('Show_Paquetes_contrato/', Show_Paquetes_contrato, name="Show_Paquetes_contrato"),
    path('Show_Formas_de_pago/', Show_Formas_de_pago, name="Show_Formas_de_pago"),
    path('Show_Viajeros/', Show_Viajeros, name="Show_Viajeros"),
    path('Show_PAI_VIA/', Show_PAI_VIA, name="Show_PAI_VIA"),
    path('Show_Registro_viajeros/', Show_Registro_viajeros, name="Show_Registro_viajeros"),
    path('Show_PAI_VIA/', Show_PAI_VIA, name="Show_PAI_VIA"),
    path('Show_Registro_viajeros/', Show_Registro_viajeros, name="Show_Registro_viajeros"),
    path('Show_Detalle_viajeros/', Show_Detalle_viajeros, name="Show_Detalle_viajeros"),
    path('Show_Participantes/', Show_Participantes, name="Show_Participantes"),
    path('Show_Puntuaciones/', Show_Puntuaciones, name="Show_Puntuaciones"),
    
]