from typing import Tuple
from django.db import models
from django.db.models.deletion import CASCADE
from compositefk.fields import CompositeForeignKey
from django.db.models.fields import IntegerField

#Proyecto  

class Bancos(models.Model):
    id_banco = models.IntegerField(primary_key=True)
    nombre_banco = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_banco

    class Meta:
        db_table = 'cgr_bancos'
        ordering = ['id_banco']

class Clientes(models.Model):
    PERSONA = (
        ('natural','Natural'),
        ('juridico','Juridico'),
    )
    doc_identidad_o_rif = models.IntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=30)
    tipo_cliente = models.CharField(max_length=10, choices=PERSONA)
    primer_apellido = models.CharField(max_length=30, null=True, blank=True)
    segundo_apellido = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.doc_identidad_o_rif)

    class Meta:
        db_table = 'cgr_clientes'
        ordering = ['doc_identidad_o_rif']

class Areas_de_interes(models.Model):
    id_areas_de_interes = models.IntegerField(primary_key=True)
    nombre_area_de_interes = models.CharField(max_length=30, unique=True)
    descripcion_area_de_interes = models.TextField(max_length=255)

    def __str__(self):
        return self.nombre_area_de_interes

    class Meta:
        db_table = 'cgr_areas_de_interes'
        ordering = ['id_areas_de_interes']

class Paises(models.Model):
    REGIONES = (
        ('EU','Europa'),
        ('AF_MO','Africa & Medio Oriente'),
        ('AU_NZ_PAC','Australia, Nueva Zelanda & Pacifico'),
        ('AS','Asia'),
        ('MEX_CEN_SUR','Mexico, Centro & Sur America'),
        ('USA_CAN_CAR','USA, Canada & Caribe'),
    )
    CONTINENTES = (
        ('Asia','Asica'),
        ('Africa','Africa'),
        ('Oceania','Oceania'),
        ('Europa','Europa'),
        ('America','America'),
    )
    id_pais = models.IntegerField(primary_key=True)
    nombre_pais = models.CharField( max_length=30)
    region_pais = models.CharField(max_length=15, choices=REGIONES)
    continente_pais = models.CharField(max_length=15, choices=CONTINENTES)
    nacionalidad = models.CharField(max_length=60)
    descripcion_pais = models.TextField(max_length=255)

    def __str__(self):
        return self.nombre_pais

    class Meta:
        db_table = 'cgr_paises'
        ordering = ['id_pais']

class Rallies(models.Model):
    CATEGORIA = (
        ('individual','Individual'),
        ('pareja','Pareja'),
    )
    id_rally = models.IntegerField(primary_key=True)
    nombre_rally = models.CharField(max_length=30)
    costo_participante = models.IntegerField()
    f_inicio = models.DateField()
    f_fin = models.DateField()
    tipo_rally = models.CharField(max_length=15, choices=CATEGORIA)
    duracion = models.IntegerField()
    total_cupo_participante = models.IntegerField()

    def __str__(self):
        return self.nombre_rally

    class Meta:
        db_table = 'cgr_rallies'
        ordering = ['id_rally']

class Premios(models.Model):
    PREMIO = (
        (1,'1er'),
        (2,'2do'),
        (3,'3ro'),
    )
    id_premio = models.IntegerField(primary_key=True)
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, related_name='id_rally_pre', db_column='id_rally')
    posicion = models.IntegerField(choices=PREMIO)
    descripcion_premio = models.TextField(max_length=255)

    def __str__(self):
        return 'Rally: ' + self.id_rally + ', ' + 'Posicion: ' + str(self.posicion)

    class Meta:

        unique_together = [('id_premio', 'id_rally')]

        db_table = 'cgr_premios'
        ordering = ['id_premio']

class Ciudades(models.Model):
    DESTINO = (
        ('localidad','Localidad'),
        ('ciudad','Ciudad'),
    )
    id_ciudad = models.IntegerField(primary_key=True)
    id_pais = models.ForeignKey(Paises, on_delete=models.CASCADE, related_name='id_pais_ciu', db_column='id_pais')
    nombre_ciudad = models.CharField(max_length=30)
    tipo_ciudad = models.CharField(choices=DESTINO, max_length=15)
    descripcion_ciudad = models.TextField(max_length=255)

    def __str__(self):
        return self.nombre_ciudad

    class Meta:

        unique_together = [('id_ciudad', 'id_pais')]

        db_table = 'cgr_ciudades'
        ordering = ['id_ciudad']

class Atracciones(models.Model):
    id_atraccion = models.IntegerField(primary_key=True)
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    nombre_atraccion = models.CharField(max_length=30)
    descripcion_atraccion = models.TextField(max_length=255)

    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return self.nombre_atraccion

    class Meta:

        unique_together = [('id_ciudad', 'id_pais', 'id_atraccion')]

        db_table = 'cgr_atracciones'
        ordering = ['id_atraccion']

class Circuitos(models.Model):
    orden_circuito = models.IntegerField(primary_key=True)
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, null=False, related_name='id_rally_cir', db_column='id_rally')
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    maxdias = models.IntegerField()

    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return str(self.orden_circuito) + '- ' + self.id_rally + ' c: ' + str(self.id_ciudad) + ' p: ' + str(self.id_pais)

    class Meta:

        unique_together = [('orden_circuito', 'id_rally', 'id_ciudad', 'id_pais')]

        db_table = 'cgr_circuitos'
        ordering = ['orden_circuito']

class ART_CIR(models.Model):
    id_atraccion = models.IntegerField(primary_key=True)
    id_ciudad_at = models.IntegerField()
    id_pais_at = models.IntegerField()
    id_circuito = models.IntegerField()
    id_rally_cir = models.IntegerField()
    id_ciudad_cir = models.IntegerField()
    id_pais_cir = models.IntegerField()
    orden = models.IntegerField(null=True, blank = True)

    lugar = CompositeForeignKey(Atracciones, on_delete=CASCADE, to_fields={'id_atraccion': 'id_atraccion','id_ciudad': 'id_ciudad_at', 'id_pais': 'id_pais_at'})
    recorrido = CompositeForeignKey(Circuitos, on_delete=CASCADE, to_fields={'orden_circuito': 'id_circuito', 'id_rally': 'id_rally_cir', 'id_ciudad': 'id_ciudad_cir', 'id_pais': 'id_pais_cir'})

    def __str__(self):
        return str(self.id_atraccion) + str(self.id_ciudad_at) + str(self.id_pais_at) + str(self.id_circuito) + str(self.id_rally_cir) + str(self.id_ciudad_cir) + str(self.id_pais_cir)


    class Meta:

        unique_together = [('id_atraccion', 'id_ciudad_at', 'id_pais_at', 'id_circuito', 'id_rally_cir', 'id_ciudad_cir', 'id_pais_cir')]

        db_table = 'cgr_art_cir'
        ordering = ['id_atraccion']

class Agencias_de_viajes(models.Model):
    OPERACION = (
        ('T','Tour Operator'),
        ('W','Wholesaler'),
        ('R','Ratailer'),
        ('M','Mixta'),
    )
    ALCANCE = (
        ('I','Internacional'),
        ('N','Nacional'),
        ('L','Local'),
    )
    id_agencia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    tipo_de_operacion = models.CharField(choices=OPERACION, max_length=1)
    alcance_geografico = models.CharField(choices=ALCANCE, max_length=1)
    web = models.CharField(null=True, blank = True, max_length=30)
    telefono = models.IntegerField(null=True, blank = True)
    calle_av = models.TextField(null=True, blank = True, max_length=255)
    descripcion = models.TextField(null=True, blank = True, max_length=255)
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()

    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cgr_agencias_de_viajes'
        ordering = ['id_agencia']

class AGE_AGE(models.Model):
    id_agencia = models.IntegerField(primary_key=True)
    id_socio = models.IntegerField()
    f_inicio = models.DateField()
    f_fin = models.DateField(null=True, blank = True)

    colegas = CompositeForeignKey(Agencias_de_viajes, on_delete=CASCADE, to_fields={'id_agencia': 'id_agencia', 'id_agencia': 'id_socio'})

    def __str__(self):
        return 'a: ' + self.id_agencia + ', ' + 's: ' + self.id_socio


    class Meta:

        unique_together = [('id_agencia', 'id_socio')]

        db_table = 'cgr_age_age'
        ordering = ['id_agencia']

class Cupos(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_cupos', db_column='id_agencia', primary_key=True)
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, related_name='id_rally_cupos', db_column='id_rally')
    cantidad = models.IntegerField(null=True, blank = True)

    def __str__(self):
        return 'A: ' + self.id_agencia + ', ' + 'R: ' + self.id_rally


    class Meta:

        unique_together = [('id_agencia', 'id_rally')]

        db_table = 'cgr_cupo'
        ordering = ['id_agencia']

class Registro_clientes(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='id_clientes_registro', db_column='doc_identidad_o_rif', primary_key=True)
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_registro', db_column='id_agencia')
    f_registro = models.DateField()
    numero_registro = models.IntegerField()

    def __str__(self):
        return 'C: ' + self.id_cliente + ', ' + 'A: ' + self.id_agencia


    class Meta:

        unique_together = [('id_agencia', 'id_cliente')]

        db_table = 'cgr_registro_clientes'
        ordering = ['id_cliente']

class Alojamientos(models.Model):
    id_alojamiento = models.IntegerField(primary_key=True)
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    nombre = models.CharField(null=True, blank = True, max_length=30)

    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return 'id: ' + str(self.id_alojamiento) + '- C: ' + str(self.id_ciudad) + ', ' + 'P: ' + str(self.id_pais)


    class Meta:
        db_table = 'cgr_alojamientos'
        ordering = ['id_alojamiento']

class Proveedores(models.Model):
    CATEGORIA = (
        ('exclusivo','Exclusivo'),
        ('multiagencias','Multiagencias'),
    )
    id_proveedor = models.IntegerField(primary_key=True)
    id_alojamiento = models.ForeignKey(Alojamientos, on_delete=models.CASCADE, related_name='id_alojamiento_proveedor', db_column='id_alojamiento')
    nombre_proveedor = models.CharField(null=True, blank = True, max_length=30)
    tipo_proveedor = models.CharField(max_length=15, choices=CATEGORIA, verbose_name='Tipo')

    def __str__(self):
        return self.nombre_proveedor


    class Meta:
        db_table = 'cgr_proveedores'
        ordering = ['id_proveedor']

class PRO_AGE(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_PA', db_column='id_agencia', primary_key=True)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, related_name='id_proveedor_PA', db_column='id_proveedor')
    f_inicio = models.DateField()
    f_fin = models.DateField(null=True, blank = True)

    def __str__(self):
        return 'A: ' + self.id_agencia + ', ' + 'P: ' + self.id_proveedor


    class Meta:

        unique_together = [('id_agencia', 'id_proveedor')]

        db_table = 'cgr_pro_age'
        ordering = ['id_agencia']

class Asesores_de_viajes(models.Model):
    id_asesor = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(null=True, blank=True, max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()

    def __str__(self):
        return self.primer_apellido + ', ' + self.primer_nombre


    class Meta:
        db_table = 'cgr_asesores_de_viajes'
        ordering = ['id_asesor']

class Paquetes(models.Model):
    id_paquete = models.IntegerField(primary_key=True)
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_pa', db_column='id_agencia')
    nombre_paquete = models.CharField(max_length=30)
    duracion_en_dias = models.IntegerField()
    descripcion_turistica = models.TextField(max_length=255)
    disponible = models.BooleanField(null=True, blank=True)
    numero_personas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.id_agencia + '- ' + self.nombre_paquete

    class Meta:

        unique_together = [('id_agencia', 'id_agencia')]

        db_table = 'cgr_paquetes'
        ordering = ['id_agencia']

class Especializaciones(models.Model):
    id_especializacion = models.IntegerField(primary_key=True)
    id_areas_de_interes = models.ForeignKey(Areas_de_interes, on_delete=models.CASCADE, related_name='id_area_es', db_column='id_areas_de_interes')
    id_atraccion = models.IntegerField()
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia_es', db_column='id_agencia')
    id_paquete = models.IntegerField()
    id_agencia_paquete = models.IntegerField()
    id_asesor = models.ForeignKey(Asesores_de_viajes, on_delete=models.CASCADE, related_name='id_asesor_es', db_column='id_asesor')
    comentarios = models.TextField(max_length=255)

    paquete = CompositeForeignKey(Paquetes, on_delete=CASCADE, to_fields={'id_agencia': 'id_paquete', 'id_agencia': 'id_agencia_paquete'})
    lugar = CompositeForeignKey(Atracciones, on_delete=CASCADE, to_fields={'id_atraccion': 'id_atraccion','id_ciudad': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return str(self.id_especializacion) + '-' + self.id_areas_de_interes

    class Meta:

        unique_together = [('id_areas_de_interes', 'id_especializacion')]

        db_table = 'cgr_especializaciones'
        ordering = ['id_especializacion']

class Precio_paquetes(models.Model):
    f_inicio = models.DateField(primary_key=True)
    id_paquete = models.IntegerField()
    id_agencia = models.IntegerField()
    f_fin = models.DateField(null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)

    paquete = CompositeForeignKey(Paquetes, on_delete=CASCADE, to_fields={'id_agencia': 'id_paquete', 'id_agencia': 'id_agencia'})

    def __str__(self):
        return self.f_inicio + '-' + str(self.id_paquete) + '-' + str(self.id_agencia)


    class Meta:

        unique_together = [('f_inicio', 'id_paquete', 'id_agencia')]

        db_table = 'cgr_precio_paquetes'
        ordering = ['f_inicio']

class Calendarios_anuales(models.Model):
    f_salida = models.DateField(primary_key=True)
    id_paquete = models.IntegerField()
    id_agencia = models.IntegerField()
    descripcion = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.f_salida + '-' + str(self.id_paquete) + '-' + str(self.id_agencia)

    class Meta:

        unique_together = [('f_salida', 'id_paquete', 'id_agencia')]

        db_table = 'cgr_calendarios_anuales'
        ordering = ['f_salida']

class Descuentos(models.Model):
    DESCUENTO = (
        ('descnino','Descuento niño'),
        ('adultos','Adultos'),
        ('general','General'),
        ('viajerosgratis','Viaje gratis'),
        ('otro','Otro'),
    )
    id_descuento = models.IntegerField(primary_key=True)
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_des', db_column='id_agencia')
    f_inicio = models.DateField()
    tipo_descuento = models.CharField(max_length=20, choices=DESCUENTO)
    f_fin = models.DateField(null=True, blank=True)
    cant_per_gratis = models.IntegerField(null=True, blank=True)
    porcentaje = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id_descuento) + '-' + self.id_agencia

    class Meta:

        unique_together = [('id_descuento', 'id_agencia')]

        db_table = 'cgr_descuentos'
        ordering = ['id_descuento']

class Intinerarios(models.Model):
    orden = models.IntegerField(primary_key=True)
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    id_agencia = models.IntegerField()
    id_paquete = models.IntegerField()
    tiempo_estadia = models.IntegerField()

    paquete = CompositeForeignKey(Paquetes, on_delete=CASCADE, to_fields={'id_agencia': 'id_paquete', 'id_agencia': 'id_agencia'})
    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return str(self.orden) + '- ' + str(self.id_paquete) + '-' + str(self.id_agencia) + ' ' + str(self.id_ciudad) + ', ' + str(self.id_pais)


    class Meta:

        unique_together = [('orden', 'id_ciudad', 'id_pais', 'id_agencia', 'id_paquete')]

        db_table = 'cgr_intinerarios'
        ordering = ['orden']

class INT_ATR(models.Model):
    id_intinerario = models.IntegerField(primary_key=True)
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    id_agencia = models.IntegerField()
    id_paquete = models.IntegerField()
    id_atraccion = models.IntegerField()
    id_ciudad_at = models.IntegerField()
    id_pais_at = models.IntegerField()
    orden_visita = models.IntegerField()

    paquete = CompositeForeignKey(Intinerarios, on_delete=CASCADE, to_fields={'orden': 'id_intinerario', 'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais', 'id_agencia': 'id_agencia', 'id_paquete': 'id_paquete'})
    lugar = CompositeForeignKey(Atracciones, on_delete=CASCADE, to_fields={'id_atraccion': 'id_atraccion', 'id_pais': 'id_pais_at', 'id_ciudad': 'id_ciudad_at'})


    def __str__(self):
        return  str(self.id_intinerario) + '-' + str(self.id_agencia) + '-' + str(self.paquete) + '-' + str(self.id_atraccion) + '-' + str(self.id_ciudad) + '-' + str(self.id_pais)

    class Meta:

        unique_together = [('id_intinerario', 'id_ciudad', 'id_pais', 'id_agencia', 'id_paquete', 'id_atraccion', 'id_ciudad_at', 'id_pais_at')]

        db_table = 'cgr_int_atr'
        ordering = ['id_intinerario']

class Detalle_servicios(models.Model):
    BOLETO = {
        ('boleto_avion', 'Boleto de avion'),
        ('boleto_tren', 'Boleto de tren'),
        ('boleto_autobus', 'Boleto de Autobus'),
        ('cama_alq', 'Cama de alquiler'),
        ('alojamiento', 'Alojamiento'),
        ('otro', 'otros'),
    }
    id_detalle_servicio = models.IntegerField(primary_key=True)
    id_intinerario = models.IntegerField()
    id_paquete = models.IntegerField()
    id_agencia = models.IntegerField()
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    tipo_detalle = models.CharField(max_length=30, choices=BOLETO)
    descripcion = models.CharField(max_length=255)
    comida = models.BooleanField(null=True, blank=True)

    paquete = CompositeForeignKey(Intinerarios, on_delete=CASCADE, to_fields={'orden': 'id_intinerario', 'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais', 'id_agencia': 'id_agencia', 'id_paquete': 'id_paquete'})


    def __str__(self):
        return str(self.id_detalle_servicio) + '-' + str(self.id_intinerario) + '-' + str(self.id_agencia) + '-' + str(self.paquete) + '-' + str(self.id_ciudad) + '-' + str(self.id_pais)

    class Meta:

        unique_together = [('id_intinerario', 'id_ciudad', 'id_pais', 'id_agencia', 'id_paquete', 'id_detalle_servicio')]

        db_table = 'cgr_Detalle_servicios'
        ordering = ['id_detalle_servicio']

class ALO_DET(models.Model):
    id_detalle_servicio = models.IntegerField(primary_key=True)
    id_intinerario = models.IntegerField()
    id_paquete = models.IntegerField()
    id_agencia = models.IntegerField()
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    id_alojamiento = models.ForeignKey(Alojamientos, on_delete=models.CASCADE, related_name='id_clientes_ALO', db_column='id_alojamiento')

    detalle = CompositeForeignKey(Detalle_servicios, on_delete=CASCADE, to_fields={'id_detalle_servicio': 'id_detalle_servicio','id_intinerario': 'id_intinerario', 'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais', 'id_agencia': 'id_agencia', 'id_paquete': 'id_paquete'})


    def __str__(self):
        return str(self.id_detalle_servicio) + '-' +  str(self.id_intinerario) + '-' + str(self.id_agencia) + '-' + str(self.paquete) + '-' + str(self.id_ciudad) + '-' + str(self.id_pais) + '-' + str(self.id_alojamiento)

    class Meta:

        unique_together = [('id_intinerario', 'id_ciudad', 'id_pais', 'id_agencia', 'id_paquete', 'id_alojamiento', 'id_detalle_servicio')]

        db_table = 'cgr_alo_det'
        ordering = ['id_detalle_servicio']

class Instrumento_de_pago(models.Model):
    INSTRUMENTO = {
        ('TDC', 'Tarjeta de Credito'),
        ('TDD', 'Tarjeta de Debito'),
        ('ctabanco', 'Cuanta Bancaria'),
        ('zelle', 'Zelle'),
    }
    id_instrumento = models.IntegerField(primary_key=True)
    doc_identidad_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='id_doc_iden_cli_ins', db_column='doc_identidad_o_rif')
    monto = models.IntegerField()
    tipo_instrumento = models.CharField(max_length=30, choices=INSTRUMENTO)
    id_banco = models.ForeignKey(Bancos, on_delete=models.CASCADE, related_name='id_banco_inst', null=True, blank=True, db_column='id_banco')
    numero_zelle = models.IntegerField(null=True, blank=True)
    email_zelle = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return 'id: ' + str(self.id_instrumento) + ' - ' + str(self.doc_identidad_cliente) 

    class Meta:

        unique_together = [('id_instrumento', 'doc_identidad_cliente')]

        db_table = 'cgr_instrumento_de_pago'
        ordering = ['id_instrumento']

class Paquetes_contrato(models.Model):
    numero_factura = models.IntegerField(primary_key=True)
    id_paquete = models.IntegerField()
    id_agencia = models.IntegerField()
    id_reg_cliente = models.IntegerField()
    id_reg_agencia = models.IntegerField()
    id_asesor = models.ForeignKey(Asesores_de_viajes, on_delete=models.CASCADE, related_name='id_asesor_paq', null=True, blank=True, db_column='id_asesor')
    presupuesto = models.IntegerField()
    f_aprobacion = models.DateField()
    f_emision = models.DateField()
    email_validacion = models.CharField(max_length=30)
    total_costo_calculado = models.IntegerField()
    numero_viajeros = models.IntegerField()
    f_viajes = models.DateField()

    registro = CompositeForeignKey(Registro_clientes, on_delete=CASCADE, to_fields={'id_cliente': 'id_reg_cliente','id_agencia': 'id_reg_agencia'})
    paquete = CompositeForeignKey(Paquetes, on_delete=CASCADE, to_fields={'id_agencia': 'id_paquete','id_agencia': 'id_agencia'})

    def __str__(self):
        return str(self.numero_factura)

    class Meta:
        db_table = 'cgr_paquetes_contrato'
        ordering = ['numero_factura']

class Formas_de_pago(models.Model):
    TRAMITES = {
        ('parcial', 'Parcial'),
        ('cuotas', 'Cuotas'),
    }
    id_instrumento = models.IntegerField(primary_key=True)
    id_cliente = models.IntegerField()
    id_paquete_contrato = models.ForeignKey(Paquetes_contrato, on_delete=models.CASCADE, related_name='id_paquete_contrato', db_column='numero_factura')
    tipo_forma_de_pago = models.CharField(max_length=30, choices=TRAMITES, null=True, blank=True)

    pago_instrumento = CompositeForeignKey(Instrumento_de_pago, on_delete=CASCADE, to_fields={'id_instrumento': 'id_instrumento','doc_identidad_cliente': 'id_cliente'})

    def __str__(self):
        return str(self.id_instrumento)

    class Meta:

        unique_together = [('id_instrumento', 'id_cliente', 'id_paquete_contrato')]

        db_table = 'cgr_formas_de_pago'
        ordering = ['id_instrumento']

class Viajeros(models.Model):
    GENERO = {
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    }
    id_de_identidad = models.IntegerField(primary_key=True)
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    id_paquete_contrato = models.ForeignKey(Paquetes_contrato, on_delete=models.CASCADE, related_name='id_paquete_viajeros', db_column='numero_factura')
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, null=True, blank=True)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=GENERO)
    f_nacimiento = models.DateField()

    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return str(self.id_de_identidad)

    class Meta:
        db_table = 'cgr_viajeros'
        ordering = ['id_de_identidad']

class PAI_VIA(models.Model):
    id_viajero = models.ForeignKey(Viajeros, on_delete=models.CASCADE, related_name='id_viajero_via', db_column='id_de_identidad', primary_key=True)
    id_pais = models.ForeignKey(Paises, on_delete=models.CASCADE, related_name='id_pais_via', db_column='id_pais')
    nro_de_pasaporte = models.IntegerField()

    def __str__(self):
        return self.id_viajero + ' ' + self.id_pais

    class Meta:
        db_table = 'cgr_paq_via'
        ordering = ['id_viajero']

class Registro_viajeros(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_reg_via', db_column='id_agencia', primary_key=True)
    id_viajero = models.ForeignKey(Viajeros, on_delete=models.CASCADE, related_name='id_viajero_reg_via', db_column='id_de_identidad')
    f_registro = models.DateField()
    nro_registro = models.IntegerField()

    def __str__(self):
        return self.id_agencia + ' ' + self.id_viajero

    class Meta:

        unique_together = [('id_viajero', 'id_agencia')]

        db_table = 'cgr_registro_viajeros'
        ordering = ['id_viajero']

class Detalle_viajeros(models.Model):
    id_viajero = models.IntegerField(primary_key=True)
    id_agencia = models.IntegerField()
    id_paquete_contrato = models.ForeignKey(Paquetes_contrato, on_delete=models.CASCADE, related_name='id_paq_cont_det', db_column='numero_factura')

    traveler = CompositeForeignKey(Registro_viajeros, on_delete=CASCADE, to_fields={'id_viajero': 'id_viajero', 'id_agencia': 'id_agencia'})

    def __str__(self):
        return 'v: ' + self.id_viajero + ' a: ' + self.id_agencia + ' ' + self.id_paquete_contrato

    class Meta:

        unique_together = [('id_viajero', 'id_agencia', 'id_paquete_contrato')]

        db_table = 'cgr_detalle_viajeros'
        ordering = ['id_viajero']

class Participantes(models.Model):
    id_partipante = models.IntegerField(primary_key=True)
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, related_name='id_participantes_rally', db_column='id_rally')
    id_via_agencia = models.IntegerField(null=True, blank=True)
    id_via_viajero = models.IntegerField(null=True, blank=True)
    id_cli_cliente = models.IntegerField(null=True, blank=True)
    id_cli_agencia = models.IntegerField(null=True, blank=True)
    equipo = models.BinaryField(null=True, blank=True)
    posicion = models.IntegerField(null=True, blank=True)

    viajero = CompositeForeignKey(Registro_viajeros, on_delete=CASCADE, to_fields={'id_viajero': 'id_via_viajero', 'id_agencia': 'id_via_agencia'})
    cliente = CompositeForeignKey(Registro_clientes, on_delete=CASCADE, to_fields={'id_cliente': 'id_cli_cliente', 'id_agencia': 'id_cli_agencia'})

    def __str__(self):
        return 'r' + self.id_rally + ' ' + str(self.id_partipante)

    class Meta:

        unique_together = [('id_rally', 'id_partipante')]

        db_table = 'cgr_participantes'
        ordering = ['id_partipante']

class Puntuaciones(models.Model):
    id_puntuacion = models.IntegerField(primary_key=True)
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, related_name='id_puntuacion_rally', null=True, blank=True, db_column='id_rally')
    id_paquete_contrato = models.ForeignKey(Paquetes_contrato, on_delete=models.CASCADE, related_name='id_paq_cont_puntuacion', null=True, blank=True, db_column='numero_factura')
    id_ciudad = models.IntegerField(null=True, blank=True)
    id_pais = models.IntegerField(null=True, blank=True)
    id_atraccion = models.IntegerField(null=True, blank=True)

    lugar = CompositeForeignKey(Atracciones, on_delete=CASCADE, to_fields={'id_atraccion': 'id_atraccion','id_ciudad': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return str(self.id_puntuacion)

    class Meta:
        db_table = 'cgr_puntuaciones'
        ordering = ['id_puntuacion']







#TEST MODEL
'''
class Test_Departamentos(models.Model):

    deptno = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    loc = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'departamentos'
        ordering = ['deptno']

class Test_Empleados(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id', null=False)
    cedula = models.IntegerField(verbose_name='cedula', null=False)
    nombre = models.CharField(verbose_name='Nombre', max_length=30, null=False)
    apellido = models.CharField(verbose_name='Apellido', max_length=30, null=False)
    id_dept = models.ForeignKey(Test_Departamentos,on_delete=CASCADE, verbose_name='id_dept', null=False, db_column='id_dept')
    salario = models.IntegerField(verbose_name='Salario', null=True, blank=True)
    cargo = models.CharField(verbose_name='Cargo', null=True, blank=True, max_length=30)
    comision = models.IntegerField(verbose_name='Comision', null=True, blank=True)
    id_jefe = models.IntegerField()
    id_ced_jefe = models.IntegerField()

    jefe = CompositeForeignKey('self', on_delete=CASCADE, to_fields={'id': 'id_jefe', 'cedula': 'id_ced_jefe'})

    def __str__(self):
        return str(self.id) + ', ' + str(self.cedula)
    
    class Meta:

        unique_together = [('id', 'cedula'),]

        db_table = 'empleados'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
'''