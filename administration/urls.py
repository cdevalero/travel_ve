from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

    #test
    path('', Show_Agencias_de_viajes, name="Show_Agencia_de_viajes"),

    # Delete
    path('Delete_bancos/<int:id>', Delete_Bancos, name="Delete_bancos"),
    path('Delete_Clientes/<int:id>', Delete_Clientes, name="Delete_Clientes"),
    path('Delete_Areas_de_interes/<int:id>', Delete_Areas_de_interes, name="Delete_Areas_de_interes"),
    path('Delete_paises/<int:id>', Delete_Paises, name="Delete_paises"),
    path('Delete_rallies/<int:id>', Delete_Rallies, name="Delete_rallies"),
    path('Delete_premios/<int:id>', Delete_Premios, name="Delete_premios"),
    path('Delete_Ciudades/<int:id>', Delete_Ciudades, name="Delete_Ciudades"),
    path('Delete_Atracciones/<int:id>', Delete_Atracciones, name="Delete_Atracciones"),
    path('Delete_Circuitos/<int:id>', Delete_Circuitos, name="Delete_Circuitos"),
    path('Delete_atr_cir/<int:id>', Delete_ATR_CIR, name="Delete_atr_cir"),
    path('Delete_Agencia_de_viajes/<int:id>', Delete_Agencia_de_viajes, name="Delete_Agencia_de_viajes"),
    path('Delete_AGE_AGE/<int:id>', Delete_AGE_AGE, name="Delete_AGE_AGE"),
    path('Delete_Cupos/<int:id>', Delete_Cupos, name="Delete_Cupos"),
    path('Delete_Registro_clientes/<int:id>', Delete_Registro_clientes, name="Delete_Registro_clientes"),
    path('Delete_Alojamientos/<int:id>', Delete_Alojamientos, name="Delete_Alojamientos"),
    path('Delete_Proveedores/<int:id>', Delete_Proveedores, name="Delete_Proveedores"),
    path('Delete_pro_age/<int:id>', Delete_PRO_AGE, name="Delete_pro_age"),
    path('Delete_Asesores_de_viajes/<int:id>', Delete_Asesores_de_viajes, name="Delete_Asesores_de_viajes"),
    path('Delete_Paquetes/<int:id>', Delete_Paquetes, name="Delete_Paquetes"),
    path('Delete_Especializaciones/<int:id>', Delete_Especializaciones, name="Delete_Especializaciones"),
    path('Delete_Precios_paquetes/<int:id>', Delete_Precios_paquetes, name="Delete_Precios_paquetes"),
    path('Delete_Calendarios_anuales/<int:id>', Delete_Calendarios_anuales, name="Delete_Calendarios_anuales"),
    path('Delete_Descuentos/<int:id>', Delete_Descuentos, name="Delete_Descuentos"),
    path('Delete_Intinerarios/<int:id>', Delete_Intinerarios, name="Delete_Intinerarios"),
    path('Delete_ITN_ATR/<int:id>', Delete_ITN_ATR, name="Delete_ITN_ATR"),
    path('Delete_Detalles_servicios/<int:id>', Delete_Detalles_servicios, name="Delete_Detalles_servicios"),
    path('Delete_ALO_DET/<int:id>', Delete_ALO_DET, name="Delete_ALO_DET"),
    path('Delete_Instrumentos_de_pago/<int:id>', Delete_Instrumentos_de_pago, name="Delete_Instrumentos_de_pago"),
    path('Delete_Paquetes_contrato/<int:id>', Delete_Paquetes_contrato, name="Delete_Paquetes_contrato"),
    path('Delete_Formas_de_pago/<int:id>', Delete_Formas_de_pago, name="Delete_Formas_de_pago"),
    path('Delete_Viajeros/<int:id>', Delete_Viajeros, name="Delete_Viajeros"),
    path('Delete_PAI_VIA/<int:id>', Delete_PAI_VIA, name="Delete_PAI_VIA"),
    path('Delete_Registro_viajeros/<int:id>', Delete_Registro_viajeros, name="Delete_Registro_viajeros"),
    path('Delete_Detalle_viajeros/<int:id>', Delete_Detalle_viajeros, name="Delete_Detalle_viajeros"),
    path('Delete_Participantes/<int:id>', Delete_Participantes, name="Delete_Participantes"),
    path('Delete_Puntuaciones/<int:id>', Delete_Puntuaciones, name="Delete_Puntuaciones"),

    #Add
    path('Add_bancos/', Add_Bancos, name="Add_bancos"),
    path('Add_Clientes/', Add_Clientes, name="Add_Clientes"),
    path('Add_Areas_de_interes/', Add_Areas_de_interes, name="Add_Areas_de_interes"),
    path('Add_paises/', Add_Paises, name="Add_paises"),
    path('Add_rallies/', Add_Rallies, name="Add_rallies"),
    path('Add_premios/', Add_Premios, name="Add_premios"),
    path('Add_Ciudades/', Add_Ciudades, name="Add_Ciudades"),
    path('Add_Atracciones/', Add_Atracciones, name="Add_Atracciones"),
    path('Add_Circuitos/', Add_Circuitos, name="Add_Circuitos"),
    path('Add_atr_cir/', Add_ATR_CIR, name="Add_atr_cir"),
    path('Add_Agencia_de_viajes/', Add_Agencia_de_viajes, name="Add_Agencia_de_viajes"),
    path('Add_AGE_AGE/', Add_AGE_AGE, name="Add_AGE_AGE"),
    path('Add_Cupos/', Add_Cupos, name="Add_Cupos"),
    path('Add_Registro_clientes/', Add_Registro_clientes, name="Add_Registro_clientes"),
    path('Add_Alojamientos/', Add_Alojamientos, name="Add_Alojamientos"),
    path('Add_Proveedores/', Add_Proveedores, name="Add_Proveedores"),
    path('Add_pro_age/', Add_PRO_AGE, name="Add_pro_age"),
    path('Add_Asesores_de_viajes/', Add_Asesores_de_viajes, name="Add_Asesores_de_viajes"),
    path('Add_Paquetes/', Add_Paquetes, name="Add_Paquetes"),
    path('Add_Especializaciones/', Add_Especializaciones, name="Add_Especializaciones"),
    path('Add_Precios_paquetes/', Add_Precios_paquetes, name="Add_Precios_paquetes"),
    path('Add_Calendarios_anuales/', Add_Calendarios_anuales, name="Add_Calendarios_anuales"),
    path('Add_Descuentos/', Add_Descuentos, name="Add_Descuentos"),
    path('Add_Intinerarios/', Add_Intinerarios, name="Add_Intinerarios"),
    path('Add_ITN_ATR/', Add_ITN_ATR, name="Add_ITN_ATR"),
    path('Add_Detalles_servicios/', Add_Detalles_servicios, name="Add_Detalles_servicios"),
    path('Add_ALO_DET/', Add_ALO_DET, name="Add_ALO_DET"),
    path('Add_Instrumentos_de_pago/', Add_Instrumentos_de_pago, name="Add_Instrumentos_de_pago"),
    path('Add_Paquetes_contrato/', Add_Paquetes_contrato, name="Add_Paquetes_contrato"),
    path('Add_Formas_de_pago/', Add_Formas_de_pago, name="Add_Formas_de_pago"),
    path('Add_Viajeros/', Add_Viajeros, name="Add_Viajeros"),
    path('Add_PAI_VIA/', Add_PAI_VIA, name="Add_PAI_VIA"),
    path('Add_Registro_viajeros/', Add_Registro_viajeros, name="Add_Registro_viajeros"),
    path('Add_Detalle_viajeros/', Add_Detalle_viajeros, name="Add_Detalle_viajeros"),
    path('Add_Participantes/', Add_Participantes, name="Add_Participantes"),
    path('Add_Puntuaciones/', Add_Puntuaciones, name="Add_Puntuaciones"),

    #Show
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
    path('Show_Agencia_de_viajes/', Show_Agencias_de_viajes, name="Show_Agencia_de_viajes"),
    path('Show_AGE_AGE/', Show_AGE_AGE, name="Show_AGE_AGE"),
    path('Show_Cupos/', Show_cupos, name="Show_Cupos"),
    path('Show_Registro_clientes/', Show_Registro_clientes, name="Show_Registro_clientes"),
    path('Show_Alojamientos/', Show_Alojamientos, name="Show_Alojamientos"),
    path('Show_Proveedores/', Show_Proveedores, name="Show_Proveedores"),
    path('Show_pro_age/', Show_pro_age, name="Show_pro_age"),
    path('Show_Asesores_de_viajes/', Show_Asesores_de_viajes, name="Show_Asesores_de_viajes"),
    path('Show_Paquetes/', Show_Paquetes, name="Show_Paquetes"),
    path('Show_Especializaciones/', Show_Especializaciones, name="Show_Especializaciones"),
    path('Show_Precios_paquetes/', Show_Precios_paquetes, name="Show_Precios_paquetes"),
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
    path('Show_Detalle_viajeros/', Show_Detalle_viajeros, name="Show_Detalle_viajeros"),
    path('Show_Participantes/', Show_Participantes, name="Show_Participantes"),
    path('Show_Puntuaciones/', Show_Puntuaciones, name="Show_Puntuaciones"),

    #Edit
    path('Edit_bancos/<int:id>', Edit_Bancos, name="Edit_bancos"),
    path('Edit_Clientes/<int:id>', Edit_Clientes, name="Edit_Clientes"),
    path('Edit_Areas_de_interes/<int:id>', Edit_Areas_de_interes, name="Edit_Areas_de_interes"),
    path('Edit_paises/<int:id>', Edit_Paises, name="Edit_paises"),
    path('Edit_rallies/<int:id>', Edit_Rallies, name="Edit_rallies"),
    path('Edit_premios/<int:id>', Edit_Premios, name="Edit_premios"),
    path('Edit_Ciudades/<int:id>', Edit_Ciudades, name="Edit_Ciudades"),
    path('Edit_Atracciones/<int:id>', Edit_Atracciones, name="Edit_Atracciones"),
    path('Edit_Circuitos/<int:id>', Edit_Circuitos, name="Edit_Circuitos"),
    path('Edit_atr_cir/<int:id>', Edit_ATR_CIR, name="Edit_atr_cir"),
    path('Edit_Agencia_de_viajes/<int:id>', Edit_Agencia_de_viajes, name="Edit_Agencia_de_viajes"),
    path('Edit_AGE_AGE/<int:id>', Edit_AGE_AGE, name="Edit_AGE_AGE"),
    path('Edit_Cupos/<int:id>', Edit_Cupos, name="Edit_Cupos"),
    path('Edit_Registro_clientes/<int:id>', Edit_Registro_clientes, name="Edit_Registro_clientes"),
    path('Edit_Alojamientos/<int:id>', Edit_Alojamientos, name="Edit_Alojamientos"),
    path('Edit_Proveedores/<int:id>', Edit_Proveedores, name="Edit_Proveedores"),
    path('Edit_pro_age/<int:id>', Edit_PRO_AGE, name="Edit_pro_age"),
    path('Edit_Asesores_de_viajes/<int:id>', Edit_Asesores_de_viajes, name="Edit_Asesores_de_viajes"),
    path('Edit_Paquetes/<int:id>', Edit_Paquetes, name="Edit_Paquetes"),
    path('Edit_Especializaciones/<int:id>', Edit_Especializaciones, name="Edit_Especializaciones"),
    path('Edit_Precios_paquetes/<int:id>', Edit_Precios_paquetes, name="Edit_Precios_paquetes"),
    path('Edit_Calendarios_anuales/<int:id>', Edit_Calendarios_anuales, name="Edit_Calendarios_anuales"),
    path('Edit_Descuentos/<int:id>', Edit_Descuentos, name="Edit_Descuentos"),
    path('Edit_Intinerarios/<int:id>', Edit_Intinerarios, name="Edit_Intinerarios"),
    path('Edit_ITN_ATR/<int:id>', Edit_ITN_ATR, name="Edit_ITN_ATR"),
    path('Edit_Detalles_servicios/<int:id>', Edit_Detalles_servicios, name="Edit_Detalles_servicios"),
    path('Edit_ALO_DET/<int:id>', Edit_ALO_DET, name="Edit_ALO_DET"),
    path('Edit_Instrumentos_de_pago/<int:id>', Edit_Instrumentos_de_pago, name="Edit_Instrumentos_de_pago"),
    path('Edit_Paquetes_contrato/<int:id>', Edit_Paquetes_contrato, name="Edit_Paquetes_contrato"),
    path('Edit_Formas_de_pago/<int:id>', Edit_Formas_de_pago, name="Edit_Formas_de_pago"),
    path('Edit_Viajeros/<int:id>', Edit_Viajeros, name="Edit_Viajeros"),
    path('Edit_PAI_VIA/<int:id>', Edit_PAI_VIA, name="Edit_PAI_VIA"),
    path('Edit_Registro_viajeros/<int:id>', Edit_Registro_viajeros, name="Edit_Registro_viajeros"),
    path('Edit_Detalle_viajeros/<int:id>', Edit_Detalle_viajeros, name="Edit_Detalle_viajeros"),
    path('Edit_Participantes/<int:id>', Edit_Participantes, name="Edit_Participantes"),
    path('Edit_Puntuaciones/<int:id>', Edit_Puntuaciones, name="Edit_Puntuaciones"),

]