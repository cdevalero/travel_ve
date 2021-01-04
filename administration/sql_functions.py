from django.db import connection

# Crear

def Crear_Premios(premio, rally, posicion, descripcion):
    pass

def Crear_Ciudad(ciudad, pais, nombre, tipo, descripcion):
    pass

def Crear_Atraccion(atraccion, ciudad, pais, nombre, descripcion):
    pass

def Crear_Circuito(orden, rally, ciudad, pais, dias):
    pass

def Crear_ATR_CIR(atraccion, ciudad_at, pais_at, circuito, rally_cir, ciudad_cir, pais_cir, orden):
    pass

def Crear_AGE_AGE(agencia, socio, inicio, fin):
    pass

def Crear_Cupo(agencia, rally, cantidad):
    pass

def Crear_Registro_clientes(cliente, agencia, fecha, numero): # GUIA --------
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_registro_clientes(id_cliente, id_agencia, f_registro, numero_registro) VALUES (%s, %s, %s, %s)', 
        [cliente, agencia, fecha, numero])

def Crear_PRO_AGE(agencia, proveedor, inicio, fin):
    pass

def Crear_Paquetes(paquete, agencia, nombre, duracion, descripcion, disponible, personas):
    pass

def Crear_Especializacion(especializacion, area, atraccion, ciudad, pais, agencia, paquete, agencia_paquete, asesor, comentario):
    pass

def Crear_Precio_paquete(inicio, paquete, agencia, fin, valor):
    pass

def Crear_Calendarios_anuales(salida, paquete, agencia, descripcion):
    pass

def Crear_Descuentos(descuento, agencia, inicio, tipo, fin, per_gratis, porcentaje):
    pass

def Crear_Itinerarios(orden, ciudad, pais, agencia, paquete, tiempo):
    pass

def Crear_ITN_ATR(itinerario, ciudad, pais, agencia, paquete, atraccion, ciudad_at, pais_at, orden):
    pass

def Crear_Detalle_servicio(detalle, itinerario, paquete, agencia, ciudad, pais, tipo, descripcion, comida):
    pass

def Crear_ALO_DET(detalle, itinerario, paquete, agencia, ciudad, pais, alojamiento):
    pass

def Crear_Instrumento_de_pago(instrumento, cliente, monto, tipo, banco, numero_z, email_z):
    pass

def Crear_Forma_de_pago(instrumento, cliente, paquete_contrato, tipo_forma_pago):
    pass

def Crear_PAI_VIA(viajero, pais, numero):
    pass

def Crear_Registro_viajeros(agencia, viajero, registro, numero):
    pass

def Crear_Detalle_viajero(viajero, agencia, paquete_contrato):
    pass

def Crear_Participantes(participante, rally, via_agencia, via_viajero, cli_cliente, cli_agencia, equipo, posicion):
    pass

# Borrar --------------------------------------------------------------------------------------------------------------

def Borrar_Premios(premio, rally):
    pass

def Borrar_Ciudad(ciudad, pais):
    pass

def Borrar_Atraccion(atraccion, ciudad, pais):
    pass

def Borrar_Circuito(orden, rally, ciudad, pais):
    pass

def Borrar_ATR_CIR(atraccion, ciudad_at, pais_at, circuito, rally_cir, ciudad_cir, pais_cir):
    pass

def Borrar_AGE_AGE(agencia, socio):
    pass

def Borrar_Cupo(agencia, rally):
    pass

def Borrar_Registro_clientes(cliente, agencia): #GUIA --------
    with connection.cursor() as cursor:
        cursor.execute ("DELETE FROM public.cgr_registro_clientes WHERE id_cliente=%s and id_agencia=%s ", 
        [cliente, agencia])

def Borrar_PRO_AGE(agencia, proveedor):
    pass

def Borrar_Paquetes(paquete, agencia):
    pass

def Borrar_Especializacion(especializacion, area):
    pass

def Borrar_Precio_paquete(inicio, paquete, agencia):
    pass

def Borrar_Calendarios_anuales(salida, paquete, agencia):
    pass

def Borrar_Descuentos(descuento, agencia):
    pass

def Borrar_Itinerarios(orden, ciudad, pais, agencia, paquete):
    pass

def Borrar_ITN_ATR(itinerario, ciudad, pais, agencia, paquete, atraccion, ciudad_at, pais_at):
    pass

def Borrar_Detalle_servicio(detalle, itinerario, paquete, agencia, ciudad, pais):
    pass

def Borrar_ALO_DET(detalle, itinerario, paquete, agencia, ciudad, pais, alojamiento):
    pass

def Borrar_Instrumento_de_pago(instrumento, cliente):
    pass

def Borrar_Forma_de_pago(instrumento, cliente, paquete_contrato):
    pass

def Borrar_PAI_VIA(viajero, pais):
    pass

def Borrar_Registro_viajeros(agencia, viajero):
    pass

def Borrar_Detalle_viajero(viajero, agencia, paquete_contrato):
    pass

def Borrar_Participantes(participante, rally):
    pass