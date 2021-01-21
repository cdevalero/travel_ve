from django.db import connection

# Crear

def Crear_Alojamiento(ciudad, pais, nombre):
    with connection.cursor() as cursor:
        cursor.execute ("INSERT INTO public.cgr_alojamientos(id_alojamiento, id_ciudad, id_pais, nombre)VALUES ((SELECT max(a.id_alojamiento) from cgr_alojamientos a) + 1, %s, %s, %s);",
        [ciudad, pais, nombre])

def Crear_Proveedor(alojamiento, nombre, tipo):
    with connection.cursor() as cursor:
        cursor.execute ("INSERT INTO public.cgr_proveedores(id_proveedor, id_alojamiento, nombre_proveedor, tipo_proveedor) VALUES ((SELECT max(p.id_proveedor) from cgr_proveedores p) + 1, %s, %s, %s);",
        [alojamiento, nombre, tipo])

def Crear_Asesor_viaje(nombre1, apellido1, apellido2, tlf, nombre2):
    if nombre2=='':
        nombre2=None;
    with connection.cursor() as cursor:
        cursor.execute ("INSERT INTO public.cgr_asesores_de_viajes(id_asesor, primer_nombre, primer_apellido, segundo_apellido, telefono, segundo_nombre) VALUES ((SELECT max(a.id_asesor) from cgr_asesores_de_viajes a) + 1, %s, %s, %s, %s, %s);",
        [nombre1, apellido1, apellido2, tlf, nombre2])

def Crear_Agencia(nombre, tipo, alcance, web, tlf, calle, ciudad, pais, descripcion):
    if web=='':
        web=None;
    if tlf=='':
        tlf=None;
    if calle=='':
        calle=None;
    if ciudad=='':
        ciudad=None;
    if pais=='':
        pais=None;
    if descripcion=='':
        descripcion=None;
    with connection.cursor() as cursor:
        cursor.execute ("INSERT INTO public.cgr_agencias_de_viajes(id_agencia, nombre, tipo_de_operacion, alcance_geografico, web, telefono, calle_av, id_ciudad, id_pais, descripcion)VALUES ((SELECT max(a.id_agencia) from cgr_agencias_de_viajes a) + 1, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
        [nombre, tipo, alcance, web, tlf, calle, ciudad, pais, descripcion])

def Crear_Banco(nombre_banco):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_bancos(id_banco, nombre_banco) VALUES (DEFAULT,%s)', 
        [nombre_banco])

def Crear_Pais(nombre_pais, region_pais, continente_pais, nacionalidad, descripcion_pais):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_paises(id_pais, nombre_pais, region_pais, continente_pais, nacionalidad, descripcion_pais) VALUES ((SELECT max(p.id_pais) from cgr_paises p) + 1, %s, %s, %s, %s, %s)', 
        [nombre_pais, region_pais, continente_pais, nacionalidad, descripcion_pais])

def Crear_Area_de_interes(id_areas_de_interes, nombre_area_de_interes, descripcion_area_de_interes):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_areas_de_interes(id_banco, nombre_banco) VALUES (%s, %s, %s)', 
        [id_areas_de_interes, nombre_area_de_interes, descripcion_area_de_interes])

def Crear_Rally(nombre_rally, costo_participante, f_inicio, f_fin, tipo_rally, duracion, total_cupo_participante):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_rallies(id_rally, nombre_rally, costo_participante, f_inicio, f_fin, tipo_rally, duracion, total_cupo_participante) VALUES ((SELECT max(p.id_rally) from cgr_rallies p) + 1, %s, %s, %s, %s, %s, %s, %s)', 
        [nombre_rally, costo_participante, f_inicio, f_fin, tipo_rally, duracion, total_cupo_participante])

def Crear_Premio(id_premio, id_rally, posicion, descripcion_premio):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_premios(id_premio, id_rally, posicion, descripcion_premio) VALUES (%s, %s, %s, %s)', 
        [id_premio, id_rally, posicion, descripcion_premio])

def Crear_Ciudad( pais, nombre, tipo, descripcion):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_ciudades(id_ciudad, id_pais, nombre_ciudad, tipo_ciudad, descripcion_ciudad) VALUES (DEFAULT, %s, %s, %s, %s)', 
        [ pais, nombre, tipo, descripcion])
#-------------------------------------------------------------------------------------
def Crear_Circuito(orden, rally, ciudad, pais, dias):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_circuitos(orden_circuito, id_rally, id_ciudad, id_pais, maxdias) VALUES (%s, %s, %s, %s, %s)', 
        [orden, rally, ciudad, pais, dias])

def Crear_ATR_CIR(atraccion, ciudad_at, pais_at, circuito, rally_cir, ciudad_cir, pais_cir, orden):
    if orden=='':
        orden=None;
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_atr_cir(id_atraccion, id_ciudad_at, id_pais_at, id_circuito, id_rally_cir, id_ciudad_cir, id_pais_cir, orden) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', 
        [atraccion, ciudad_at, pais_at, circuito, rally_cir, ciudad_cir, pais_cir, orden])

def Crear_AGE_AGE(agencia, socio, inicio, fin):
    if fin=='':
        fin=None;
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_age_age(id_agencia, id_socio, f_inicio, f_fin) VALUES (%s, %s, %s, %s)', 
        [agencia, socio, inicio, fin])

def Crear_Cupo(agencia, rally, cantidad):
    if cantidad=='':
        cantidad=None;
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_cupos(id_agencia, id_rally, cantidad) VALUES (%s, %s, %s)', 
        [agencia, rally, cantidad])

def Crear_Registro_clientes(cliente, agencia, fecha, numero): # GUIA --------
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_registro_clientes(id_cliente, id_agencia, f_registro, numero_registro) VALUES (%s, %s, %s, %s)', 
        [cliente, agencia, fecha, numero])

def Crear_PRO_AGE(agencia, proveedor, inicio, fin):
    if fin=='':
        fin=None;
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_pro_age(id_agencia, id_proveedor, f_inicio, f_fin) VALUES (%s, %s, %s, %s)', 
        [agencia, proveedor, inicio, fin])

def Crear_Precio_paquete(inicio, paquete, agencia, fin, valor):
    if fin=='':
        fin=None;
    if valor=='':
        valor=None;
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_precios_paquetes(f_inicio, id_paquete, id_agencia, f_fin, valor) VALUES (%s, %s, %s, %s, %s)', 
        [inicio, paquete, agencia, fin, valor])

def Crear_Calendarios_anuales(salida, paquete, agencia, descripcion):
    if descripcion=='':
        descripcion=None;
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_calendarios_anuales(f_salida, id_paquete, id_agencia, descripcion) VALUES (%s, %s, %s, %s)', 
        [salida, paquete, agencia, descripcion])

def Crear_Itinerarios(orden, ciudad, pais, agencia, paquete, tiempo):
    if tiempo=='':
        tiempo=None;
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_itinerarios(orden, id_ciudad, id_pais, id_agencia, id_paquete, tiempo_estadia) VALUES (%s, %s, %s, %s, %s, %s)', 
        [orden, ciudad, pais, agencia, paquete, tiempo])

def Crear_ITN_ATR(itinerario, ciudad, pais, agencia, paquete, atraccion, ciudad_at, pais_at, orden):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_itn_atr(id_itinerario, id_ciudad, id_pais, id_agencia, id_paquete, id_atraccion, id_ciudad_at, id_pais_at, orden_visita) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', 
        [itinerario, ciudad, pais, agencia, paquete, atraccion, ciudad_at, pais_at, orden])

def Crear_ALO_DET(detalle, itinerario, paquete, agencia, ciudad, pais, alojamiento):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_alo_det(id_detalle_servicio, id_itinerario, id_paquete, id_agencia, id_ciudad, id_pais, id_alojamiento) VALUES (%s, %s, %s, %s, %s, %s, %s)', 
        [detalle, itinerario, paquete, agencia, ciudad, pais, alojamiento])

def Crear_Forma_de_pago(instrumento, cliente, paquete_contrato, tipo_forma_pago):
    if tipo_forma_pago=='':
        tipo_forma_pago=None;
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_formas_de_pago(id_instrumento, id_cliente, id_paquete_contrato, tipo_forma_de_pago) VALUES (%s, %s, %s, %s)', 
        [instrumento, cliente, paquete_contrato, tipo_forma_pago])

def Crear_PAI_VIA(viajero, pais, numero):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_pai_via(id_viajero, id_pais, nro_de_pasaporte) VALUES (%s, %s, %s)', 
        [viajero, pais, numero])

def Crear_Registro_viajeros(agencia, viajero, registro, numero):                                                                        
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_registro_viajeros(id_agencia, id_viajero, f_registro, nro_registro) VALUES (%s, %s, %s, (SELECT max(r.nro_registro) from cgr_registro_viajeros r) + 1)', 
        [agencia, viajero, registro])

def Crear_Detalle_viajero(viajero, agencia, paquete_contrato):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_detalle_viajeros(id_viajero, id_agencia, id_paquete_contrato) VALUES (%s, %s, %s)', 
        [viajero, agencia, paquete_contrato])

# Borrar --------------------------------------------------------------------------------------------------------------

def Borrar_Circuito(orden, rally, ciudad, pais):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_circuitos WHERE orden_circuito=%s and id_rally=%s and id_ciudad=%s and id_pais=%s ", 
        [orden, rally, ciudad, pais])

def Borrar_ATR_CIR(atraccion, ciudad_at, pais_at, circuito, rally_cir, ciudad_cir, pais_cir):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_atr_cir WHERE id_atraccion=%s and id_ciudad_at=%s and id_pais_at=%s and id_circuito=%s and id_rally_cir=%s and id_ciudad_cir=%s and id_pais_cir=%s ", 
        [atraccion, ciudad_at, pais_at, circuito, rally_cir, ciudad_cir, pais_cir])

def Borrar_AGE_AGE(agencia, socio):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_age_age WHERE id_agencia=%s and id_socio=%s ", 
        [agencia, socio])

def Borrar_Cupo(agencia, rally):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_cupos WHERE id_agencia=%s and id_rally=%s ", 
        [agencia, rally])

def Borrar_Registro_clientes(cliente, agencia): #GUIA --------
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_registro_clientes WHERE id_cliente=%s and id_agencia=%s ", 
        [cliente, agencia])

def Borrar_PRO_AGE(agencia, proveedor):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_pro_age WHERE id_agencia=%s and id_proveedor=%s ", 
        [agencia, proveedor])

def Borrar_Precio_paquete(inicio, paquete, agencia):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_precios_paquetes WHERE f_inicio=%s and id_paquete=%s and id_agencia=%s ", 
        [inicio, paquete, agencia])

def Borrar_Calendarios_anuales(salida, paquete, agencia):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_calendarios_anuales WHERE f_salida=%s and id_paquete=%s and id_agencia=%s ", 
        [salida, paquete, agencia])

def Borrar_Itinerarios(orden, ciudad, pais, agencia, paquete):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_itinerarios WHERE orden=%s and id_ciudad=%s and id_pais=%s and id_agencia=%s and id_paquete=%s ", 
        [orden, ciudad, pais, agencia, paquete])

def Borrar_ITN_ATR(itinerario, ciudad, pais, agencia, paquete, atraccion, ciudad_at, pais_at):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_itn_atr WHERE id_itinerario=%s and id_ciudad=%s and id_pais=%s id_agencia=%s and id_paquete=%s and id_atraccion=%s and id_ciudad_at=%s and id_pais_at=%s ", 
        [itinerario, ciudad, pais, agencia, paquete, atraccion, ciudad_at, pais_at])

def Borrar_ALO_DET(detalle, itinerario, paquete, agencia, ciudad, pais, alojamiento):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_alo_det WHERE id_detalle_servicio=%s and id_itinerario=%s and id_paquete=%s id_agencia=%s and id_ciudad=%s and id_pais=%s and id_alojamiento=%s ", 
        [detalle, itinerario, paquete, agencia, ciudad, pais, alojamiento])

def Borrar_Forma_de_pago(instrumento, cliente, paquete_contrato):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_formas_de_pago WHERE id_instrumento=%s and id_cliente=%s and id_paquete_contrato=%s ", 
        [instrumento, cliente, paquete_contrato])

def Borrar_PAI_VIA(viajero, pais):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_pai_via WHERE id_viajero=%s and id_pais=%s ", 
        [viajero, pais])

def Borrar_Registro_viajeros(agencia, viajero):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_registro_viajeros WHERE id_agencia=%s and id_viajero=%s ", 
        [agencia, viajero])

def Borrar_Detalle_viajero(viajero, agencia, paquete_contrato):
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_detalle_viajeros WHERE id_viajero=%s and id_agencia=%s and id_paquete_contrato=%s ", 
        [viajero, agencia, paquete_contrato])

# Actualizar --------------------------------------------------------------------------------------------------------------

def Actualizar_Circuito(orden, rally, ciudad, pais, dias):
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_circuitos SET orden_circuito=%s, id_rally=%s, id_ciudad=%s, id_pais=%s, maxdias=%s WHERE orden_circuito=%s and id_rally=%s and id_ciudad=%s and id_pais=%s', 
        [orden, rally, ciudad, pais, dias, orden, rally, ciudad, pais])

def Actualizar_ATR_CIR(atraccion, ciudad_at, pais_at, circuito, rally_cir, ciudad_cir, pais_cir, orden):
    if orden=='':
        orden=None;
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_atr_cir SET id_atraccion=%s, id_ciudad_at=%s, id_pais_at=%s, id_circuito=%s, id_rally_cir=%s, id_ciudad_cir=%s, id_pais_cir=%s, orden=%s WHERE id_atraccion=%s and id_ciudad_at=%s and id_pais_at=%s and id_circuito=%s and id_rally_cir=%s and id_ciudad_cir=%s and id_pais_cir=%s', 
        [atraccion, ciudad_at, pais_at, circuito, rally_cir, ciudad_cir, pais_cir, orden, atraccion, ciudad_at, pais_at, circuito, rally_cir, ciudad_cir, pais_cir])

def Actualizar_AGE_AGE(agencia, socio, inicio, fin):
    if fin=='':
        fin=None;
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_age_age SET f_inicio=%s, f_fin=%s WHERE id_agencia=%s and id_socio=%s', 
        [inicio, fin, agencia, socio])

def Actualizar_Cupo(agencia, rally, cantidad):
    if cantidad=='':
        cantidad=None;
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_cupos SET id_agencia=%s, id_rally=%s, cantidad=%s WHERE id_agencia=%s and id_rally=%s', 
        [agencia, rally, cantidad, agencia, rally])

def Actualizar_Registro_clientes(cliente, agencia, fecha, numero): # GUIA --------
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_registro_clientes SET id_cliente=%s, id_agencia=%s, f_registro=%s, numero_registro=%s WHERE id_cliente=%s and id_agencia=%s', 
        [cliente, agencia, fecha, numero, cliente, agencia])

def Actualizar_PRO_AGE(agencia, proveedor, inicio, fin):
    if fin=='':
        fin=None;
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_pro_age SET id_agencia=%s, id_proveedor=%s, f_inicio=%s, f_fin=%s WHERE id_agencia=%s and id_proveedor=%s', 
        [agencia, proveedor, inicio, fin, agencia, proveedor])

def Actualizar_Precio_paquete(inicio, paquete, agencia, fin, valor):
    if fin=='':
        fin=None;
    if valor=='':
        valor=None;
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_precios_paquetes SET f_inicio=%s, id_paquete=%s, id_agencia=%s, f_fin=%s, valor=%s WHERE f_inicio=%s and id_paquete=%s and id_agencia=%s', 
        [inicio, paquete, agencia, fin, valor, inicio, paquete, agencia])

def Actualizar_Calendarios_anuales(salida, paquete, agencia, descripcion):
    if descripcion=='':
        descripcion=None;
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_calendarios_anuales SET f_salida=%s, id_paquete=%s, id_agencia=%s, descripcion=%s WHERE f_salida=%s and id_paquete=%s and id_agencia=%s', 
        [salida, paquete, agencia, descripcion, salida, paquete, agencia])

def Actualizar_Itinerarios(orden, ciudad, pais, agencia, paquete, tiempo):
    if tiempo=='':
        tiempo=None;
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_itinerarios SET orden=%s, id_ciudad=%s, id_pais=%s, id_agencia=%s, id_paquete=%s, tiempo_estadia=%s WHERE orden=%s and id_ciudad=%s and id_pais=%s and id_agencia=%s and id_paquete=%s', 
        [orden, ciudad, pais, agencia, paquete, tiempo, orden, ciudad, pais, agencia, paquete])

def Actualizar_ITN_ATR(itinerario, ciudad, pais, agencia, paquete, atraccion, ciudad_at, pais_at, orden):
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_itn_atr SET id_itinerario=%s, id_ciudad=%s, id_pais=%s, id_agencia=%s, id_paquete=%s, id_atraccion=%s, id_ciudad_at=%s, id_pais_at=%s, orden_visita=%s WHERE id_itinerario=%s and id_ciudad=%s and id_pais=%s and id_agencia=%s and id_paquete=%s and id_atraccion=%s and id_ciudad_at=%s and id_pais_at=%s', 
        [itinerario, ciudad, pais, agencia, paquete, atraccion, ciudad_at, pais_at, orden, itinerario, ciudad, pais, agencia, paquete, atraccion, ciudad_at, pais_at])

def Actualizar_ALO_DET(detalle, itinerario, paquete, agencia, ciudad, pais, alojamiento):
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_alo_det SET id_detalle_servicio=%s, id_itinerario=%s, id_paquete=%s, id_agencia=%s, id_ciudad=%s, id_pais=%s, id_alojamiento=%s WHERE id_detalle_servicio=%s and id_itinerario=%s and id_paquete=%s and id_agencia=%s and id_ciudad=%s and id_pais=%s and id_alojamiento=%s', 
        [detalle, itinerario, paquete, agencia, ciudad, pais, alojamiento, detalle, itinerario, paquete, agencia, ciudad, pais, alojamiento])

def Actualizar_Forma_de_pago(instrumento, cliente, paquete_contrato, tipo_forma_pago):
    if tipo_forma_pago=='':
        tipo_forma_pago=None;
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_formas_de_pago SET id_instrumento=%s, id_cliente=%s, id_paquete_contrato=%s, tipo_forma_de_pago=%s WHERE id_instrumento=%s and id_cliente=%s and id_paquete_contrato=%s', 
        [instrumento, cliente, paquete_contrato, tipo_forma_pago, instrumento, cliente, paquete_contrato])

def Actualizar_PAI_VIA(viajero, pais, numero):
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_pai_via SET id_viajero=%s, id_pais=%s, nro_de_pasaporte=%s WHERE id_viajero=%s and id_pais=%s', 
        [viajero, pais, numero, viajero, pais])

def Actualizar_Registro_viajeros(agencia, viajero, registro, numero):
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_registro_viajeros SET id_agencia=%s, id_viajero=%s, f_registro=%s, nro_registro=%s WHERE id_agencia=%s and id_viajero=%s', 
        [agencia, viajero, registro, numero, agencia, viajero])

def Actualizar_Detalle_viajero(viajero, agencia, paquete_contrato):
    with connection.cursor() as cursor:
        cursor.execute ('UPDATE public.cgr_detalle_viajeros SET id_viajero=%s, id_agencia=%s, id_paquete_contrato=%s WHERE id_viajero=%s and id_agencia=%s and id_paquete_contrato=%s', 
        [viajero, agencia, paquete_contrato, viajero, agencia, paquete_contrato])
