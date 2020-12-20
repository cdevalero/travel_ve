from typing import Tuple
from django.db import models
from django.db.models.deletion import CASCADE
from compositefk.fields import CompositeForeignKey
from django.db.models.fields import IntegerField

#Proyecto  

class Bancos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'bancos'
        ordering = ['id']

class Clientes(models.Model):
    PERSONA = (
        ('natural','Natural'),
        ('juridico','Juridico'),
    )
    doc_identidad_rif = models.IntegerField()
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=10, choices=PERSONA)

    def __str__(self):
        return str(self.doc_identidad_rif)

    class Meta:
        db_table = 'clientes'
        ordering = ['doc_identidad_rif']

class Areas_de_interes(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'areas_de_interes'
        ordering = ['id']

class Paices(models.Model):
    REGIONES = (
        ('EU','Europa'),
        ('AF_MO','Africa & Medio Oriente'),
        ('AU_NZ_PAC','Australia, Nueva Zelanda & Pacifico'),
        ('AS','Asia'),
        ('MEX_CEN_SUR','Mexico, Centro & Sur America'),
        ('USA_CAN_CAR','USA, Canada & Caribe'),
    )
    CONTINENTES = (
        ('asia','Asica'),
        ('africa','Africa'),
        ('oceania','Oceania'),
        ('europa','Europa'),
        ('america','America'),
    )
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField( max_length=30)
    region = models.CharField(max_length=15, choices=REGIONES)
    continente = models.CharField(max_length=15, choices=CONTINENTES)
    nacionalidad = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'paices'
        ordering = ['id']

class Rallies(models.Model):
    CATEGORIA = (
        ('individual','Individual'),
        ('pareja','Pareja'),
    )
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    costo_participante = models.IntegerField()
    f_inicio = models.DateField()
    f_fin = models.DateField()
    tipo = models.CharField(max_length=15, choices=CATEGORIA)
    duracion = models.IntegerField()
    total_cupo_participante = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'rallies'
        ordering = ['id']

class Premios(models.Model):
    PREMIO = (
        (1,'1er'),
        (2,'2do'),
        (3,'3ro'),
    )
    id = models.IntegerField(primary_key=True)
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, related_name='id_rally')
    posicion = models.IntegerField(choices=PREMIO)
    descripcion = models.TextField(max_length=255)

    def __str__(self):
        return 'Rally: ' + self.id_rally + ', ' + 'Posicion: ' + str(self.posicion)

    class Meta:

        unique_together = [('id', 'id_rally')]

        db_table = 'premios'
        ordering = ['id']

class Ciudades(models.Model):
    DESTINO = (
        ('localidad','Localidad'),
        ('ciudad','Ciudad'),
    )
    id = models.IntegerField(primary_key=True)
    id_pais = models.ForeignKey(Paices, on_delete=models.CASCADE, related_name='id_pais')
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(choices=DESTINO, max_length=15)
    descripcion = models.TextField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:

        unique_together = [('id', 'id_pais')]

        db_table = 'ciudades'
        ordering = ['id']

class Atracciones(models.Model):
    id = models.IntegerField(primary_key=True)
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=255)

    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return self.nombre

    class Meta:

        unique_together = [('id_ciudad', 'id_pais', 'id')]

        db_table = 'atracciones'
        ordering = ['id']

class Circuitos(models.Model):
    orden = models.IntegerField()
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, null=False, related_name='id_rally_cir')
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    maxdias = models.IntegerField()

    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return str(self.orden) + '- ' + self.id_rally + ' c: ' + str(self.id_ciudad) + ' p: ' + str(self.id_pais)

    class Meta:

        unique_together = [('orden', 'id_rally', 'id_ciudad', 'id_pais')]

        db_table = 'circuitos'
        ordering = ['orden']

class ART_CIR(models.Model):
    id_atraccion = models.IntegerField()
    id_ciudad_at = models.IntegerField()
    id_pais_at = models.IntegerField()
    id_circuito = models.IntegerField()
    id_rally_cir = models.IntegerField()
    id_ciudad_cir = models.IntegerField()
    id_pais_cir = models.IntegerField()
    orden = models.IntegerField(null=True, blank = True)

    lugar = CompositeForeignKey(Atracciones, on_delete=CASCADE, to_fields={'id': 'id_atraccion','id_ciudad': 'id_ciudad_at', 'id_pais': 'id_pais_at'})
    recorrido = CompositeForeignKey(Circuitos, on_delete=CASCADE, to_fields={'orden': 'id_circuito', 'id_rally': 'id_rally_cir', 'id_ciudad': 'id_ciudad_cir', 'id_pais': 'id_pais_cir'})

    def __str__(self):
        return str(self.id_atraccion) + str(self.id_ciudad_at) + str(self.id_pais_at) + str(self.id_circuito) + str(self.id_rally_cir) + str(self.id_ciudad_cir) + str(self.id_pais_cir)


    class Meta:

        unique_together = [('id_atraccion', 'id_ciudad_at', 'id_pais_at', 'id_circuito', 'id_rally_cir', 'id_ciudad_cir', 'id_pais_cir')]

        db_table = 'art_cir'
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
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    tipo_de_operacion = models.CharField(choices=OPERACION, max_length=1)
    alcance_geografico = models.CharField(choices=ALCANCE, max_length=1)
    web = models.CharField(null=True, blank = True, max_length=30)
    telefono = models.IntegerField(null=True, blank = True)
    calle_av = models.TextField(null=True, blank = True, max_length=255)
    descripcion = models.TextField(null=True, blank = True, max_length=255)
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()

    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'agencias_de_viajes'
        ordering = ['id']

class AGE_AGE(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia')
    id_socio = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_socio')
    f_inicio = models.DateField()
    f_fin = models.DateField(null=True, blank = True)

    def __str__(self):
        return 'a: ' + self.id_agencia + ', ' + 's: ' + self.id_socio


    class Meta:

        unique_together = [('id_agencia', 'id_socio')]

        db_table = 'age_age'
        ordering = ['id_agencia']

class Cupos(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_cupos')
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, related_name='id_rally_cupos')
    cantidad = models.IntegerField(null=True, blank = True)

    def __str__(self):
        return 'A: ' + self.id_agencia + ', ' + 'R: ' + self.id_rally


    class Meta:

        unique_together = [('id_agencia', 'id_rally')]

        db_table = 'cupo'
        ordering = ['id_agencia']

class Registro_clientes(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, related_name='id_clientes_registro')
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_registro')
    f_registro = models.DateField()
    numero_registro = models.IntegerField()

    def __str__(self):
        return 'C: ' + self.id_cliente + ', ' + 'A: ' + self.id_agencia


    class Meta:

        unique_together = [('id_agencia', 'id_cliente')]

        db_table = 'registro_clientes'
        ordering = ['id_cliente']

class Alojamientos(models.Model):
    id = models.IntegerField(primary_key=True)
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    nombre = models.CharField(null=True, blank = True, max_length=30)

    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return 'id: ' + str(self.id) + '- C: ' + str(self.id_ciudad) + ', ' + 'P: ' + str(self.id_pais)


    class Meta:
        db_table = 'alojamientos'
        ordering = ['id']

class Proveedores(models.Model):
    CATEGORIA = (
        ('exclusivo','Exclusivo'),
        ('multiagencias','Multiagencias'),
    )
    id = models.IntegerField(primary_key=True)
    id_alojamiento = models.ForeignKey(Alojamientos, on_delete=models.CASCADE, related_name='id_alojamiento_proveedor')
    nombre = models.CharField(null=True, blank = True, max_length=30)
    tipo = models.CharField(max_length=15, choices=CATEGORIA, verbose_name='Tipo')

    def __str__(self):
        return self.nombre


    class Meta:
        db_table = 'proveedores'
        ordering = ['id']

class PRO_AGE(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_PA')
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, related_name='id_proveedor_PA')
    f_inicio = models.DateField()
    f_fin = models.DateField(null=True, blank = True)

    def __str__(self):
        return 'A: ' + self.id_agencia + ', ' + 'P: ' + self.id_proveedor


    class Meta:

        unique_together = [('id_agencia', 'id_proveedor')]

        db_table = 'pro_age'
        ordering = ['id']

class Asesores_de_viajes(models.Model):
    id = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(null=True, blank=True, max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()

    def __str__(self):
        return self.primer_apellido + ', ' + self.primer_nombre


    class Meta:
        db_table = 'asesores_de_viajes'
        ordering = ['id']

class Paquetes(models.Model):
    id = models.IntegerField(primary_key=True)
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_pa')
    nombre = models.CharField(max_length=30)
    duracion_en_dias = models.IntegerField()
    descripcion_turistica = models.TextField(max_length=255)
    disponible = models.BooleanField(null=True, blank=True)
    numero_de_personas = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.id_agencia + '- ' + self.nombre

    class Meta:

        unique_together = [('id_agencia', 'id')]

        db_table = 'paquetes'
        ordering = ['id']

class Especializaciones(models.Model):
    id = models.IntegerField(primary_key=True)
    id_area = models.ForeignKey(Areas_de_interes, on_delete=models.CASCADE, related_name='id_area_es')
    id_atraccion = models.IntegerField()
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia_es')
    id_paquete = models.IntegerField()
    id_agencia_paquete = models.IntegerField()
    id_asesor = models.ForeignKey(Asesores_de_viajes, on_delete=models.CASCADE, related_name='id_asesor_es')
    comentarios = models.TextField(max_length=255)

    paquete = CompositeForeignKey(Paquetes, on_delete=CASCADE, to_fields={'id': 'id_paquete', 'id_agencia': 'id_agencia_paquete'})
    lugar = CompositeForeignKey(Atracciones, on_delete=CASCADE, to_fields={'id': 'id_atraccion','id_ciudad': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return str(self.id) + '-' + self.id_area

    class Meta:

        unique_together = [('id_area', 'id')]

        db_table = 'especializaciones'
        ordering = ['id']

class Precio_paquetes(models.Model):
    f_inicio = models.DateField()
    id_paquete = models.IntegerField()
    id_agencia = models.IntegerField()
    f_fin = models.DateField(null=True, blank=True)
    valor = models.IntegerField(null=True, blank=True)

    paquete = CompositeForeignKey(Paquetes, on_delete=CASCADE, to_fields={'id': 'id_paquete', 'id_agencia': 'id_agencia'})

    def __str__(self):
        return self.f_inicio + '-' + str(self.id_paquete) + '-' + str(self.id_agencia)


    class Meta:

        unique_together = [('f_inicio', 'id_paquete', 'id_agencia')]

        db_table = 'precio_paquetes'
        ordering = ['f_inicio']

class Calendarios_anuales(models.Model):
    f_salida = models.DateField()
    id_paquete = models.IntegerField()
    id_agencia = models.IntegerField()
    descripcion = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.f_salida + '-' + str(self.id_paquete) + '-' + str(self.id_agencia)

    class Meta:

        unique_together = [('f_salida', 'id_paquete', 'id_agencia')]

        db_table = 'calendarios_anuales'
        ordering = ['f_salida']

class Descuentos(models.Model):
    DESCUENTO = (
        ('descnino','Descuento niño'),
        ('adultos','Adultos'),
        ('general','General'),
        ('viajerosgratis','Viaje gratis'),
        ('otro','Otro'),
    )
    id = models.IntegerField(primary_key=True)
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_des')
    f_inicio = models.DateField()
    tipo = models.CharField(max_length=20, choices=DESCUENTO)
    f_fin = models.DateField(null=True, blank=True)
    cant_per_gratis = models.IntegerField(null=True, blank=True)
    porcentaje = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + '-' + self.id_agencia

    class Meta:

        unique_together = [('id', 'id_agencia')]

        db_table = 'descuentos'
        ordering = ['id']

class Intinerarios(models.Model):
    orden = models.IntegerField()
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    id_agencia = models.IntegerField()
    id_paquete = models.IntegerField()
    tiempo_estadia = models.IntegerField()

    paquete = CompositeForeignKey(Paquetes, on_delete=CASCADE, to_fields={'id': 'id_paquete', 'id_agencia': 'id_agencia'})
    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return str(self.orden) + '- ' + str(self.id_paquete) + '-' + str(self.id_agencia) + ' ' + str(self.id_ciudad) + ', ' + str(self.id_pais)


    class Meta:

        unique_together = [('orden', 'id_ciudad', 'id_pais', 'id_agencia', 'id_paquete')]

        db_table = 'intinerarios'
        ordering = ['orden']

class INT_ATR(models.Model):
    id_intinerario = models.IntegerField()
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    id_agencia = models.IntegerField()
    id_paquete = models.IntegerField()
    id_atraccion = models.ForeignKey(Atracciones, on_delete=models.CASCADE, related_name='id_atraccion_IA')
    orden_visita = models.IntegerField()

    paquete = CompositeForeignKey(Intinerarios, on_delete=CASCADE, to_fields={'orden': 'id_intinerario', 'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais', 'id_agencia': 'id_agencia', 'id_paquete': 'id_paquete'})


    def __str__(self):
        return  str(self.id_intinerario) + '-' + str(self.id_agencia) + '-' + str(self.paquete) + '-' + str(self.id_atraccion) + '-' + str(self.id_ciudad) + '-' + str(self.id_pais)

    class Meta:

        unique_together = [('id_intinerario', 'id_ciudad', 'id_pais', 'id_agencia', 'id_paquete', 'id_atraccion')]

        db_table = 'INT_ATR'
        ordering = ['id_intinerario']

class Detalle_servicio(models.Model):
    BOLETO = {
        ('boleto_avion', 'Boleto de avion'),
        ('boleto_tren', 'Boleto de tren'),
        ('boleto_autobus', 'Boleto de Autobus'),
        ('cama_alq', 'Cama de alquiler'),
        ('alojamiento', 'Alojamiento'),
        ('otro', 'otros'),
    }
    id_detalle = models.IntegerField()
    id_intinerario = models.IntegerField()
    id_paquete = models.IntegerField()
    id_agencia = models.IntegerField()
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    tipo = models.CharField(max_length=30, choices=BOLETO)
    descripcion = models.CharField(max_length=255)
    comida = models.BooleanField(null=True, blank=True)

    paquete = CompositeForeignKey(Intinerarios, on_delete=CASCADE, to_fields={'orden': 'id_intinerario', 'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais', 'id_agencia': 'id_agencia', 'id_paquete': 'id_paquete'})


    def __str__(self):
        return str(self.id_detalle) + '-' + str(self.id_intinerario) + '-' + str(self.id_agencia) + '-' + str(self.paquete) + '-' + str(self.id_ciudad) + '-' + str(self.id_pais)

    class Meta:

        unique_together = [('id_intinerario', 'id_ciudad', 'id_pais', 'id_agencia', 'id_paquete', 'id_detalle')]

        db_table = 'Detalle_servicio'
        ordering = ['id_detalle']

class ALO_DET(models.Model):
    id_detalle = models.IntegerField()
    id_intinerario = models.IntegerField()
    id_paquete = models.IntegerField()
    id_agencia = models.IntegerField()
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    id_alojamiento = models.ForeignKey(Alojamientos, on_delete=models.CASCADE, related_name='id_clientes_ALO')

    detalle = CompositeForeignKey(Detalle_servicio, on_delete=CASCADE, to_fields={'id_detalle': 'id_detalle','id_intinerario': 'id_intinerario', 'id_ciudad': 'id_ciudad', 'id_pais': 'id_pais', 'id_agencia': 'id_agencia', 'id_paquete': 'id_paquete'})


    def __str__(self):
        return str(self.id_detalle) + '-' +  str(self.id_intinerario) + '-' + str(self.id_agencia) + '-' + str(self.paquete) + '-' + str(self.id_ciudad) + '-' + str(self.id_pais) + '-' + str(self.id_alojamiento)

    class Meta:

        unique_together = [('id_intinerario', 'id_ciudad', 'id_pais', 'id_agencia', 'id_paquete', 'id_alojamiento')]

        db_table = 'ALO_DET'
        ordering = ['id_detalle']

class Instrumento_de_pago(models.Model):
    INSTRUMENTO = {
        ('TDC', 'Tarjeta de Credito'),
        ('TDD', 'Tarjeta de Debito'),
        ('ctabanco', 'Cuanta Bancaria'),
        ('zelle', 'Zelle'),
    }
    id = models.IntegerField(primary_key=True)
    doc_identidad_cliente = models.IntegerField()
    monto = models.IntegerField()
    tipo = models.CharField(max_length=30, choices=INSTRUMENTO)
    id_banco = models.ForeignKey(Bancos, on_delete=models.CASCADE, related_name='id_banco_inst', null=True, blank=True)
    numero_zelle = models.IntegerField(null=True, blank=True)
    email_zelle = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return 'id: ' + str(self.id) + ' - ' + str(self.doc_identidad_cliente) 

    class Meta:

        unique_together = [('id', 'doc_identidad_cliente')]

        db_table = 'instrumento_de_pago'
        ordering = ['id']

class Paquetes_contrato(models.Model):
    numero_factura = models.IntegerField()
    id_paquete = models.IntegerField()
    id_agencia = models.IntegerField()
    id_reg_cliente = models.IntegerField()
    id_reg_agencia = models.IntegerField()
    id_asesor = models.ForeignKey(Asesores_de_viajes, on_delete=models.CASCADE, related_name='id_asesor_paq', null=True, blank=True)
    presupuesto = models.IntegerField()
    f_aprobacion = models.DateField()
    f_emision = models.DateField()
    email_validacion = models.CharField(max_length=30)
    total_costo_calculado = models.IntegerField()
    numero_viajeros = models.IntegerField()
    f_viajes = models.DateField()

    registro = CompositeForeignKey(Registro_clientes, on_delete=CASCADE, to_fields={'id_cliente': 'id_reg_cliente','id_agencia': 'id_reg_agencia'})
    paquete = CompositeForeignKey(Paquetes, on_delete=CASCADE, to_fields={'id': 'id_paquete','id_agencia': 'id_agencia'})

    def __str__(self):
        return str(self.numero_factura)

    class Meta:
        db_table = 'paquetes_contrato'
        ordering = ['numero_factura']

class Formas_de_pago(models.Model):
    TRAMITES = {
        ('parcial', 'Parcial'),
        ('cuotas', 'Cuotas'),
    }
    id_instrumento = models.IntegerField()
    id_cliente = models.IntegerField()
    id_paquete_contrato = models.ForeignKey(Paquetes_contrato, on_delete=models.CASCADE, related_name='id_paquete_contrato')
    tipo = models.CharField(max_length=30, choices=TRAMITES, null=True, blank=True)

    pago_instrumento = CompositeForeignKey(Instrumento_de_pago, on_delete=CASCADE, to_fields={'id': 'id_instrumento','doc_identidad_cliente': 'id_cliente'})

    def __str__(self):
        return str(self.numero_factura)

    class Meta:

        unique_together = [('id_instrumento', 'id_cliente', 'id_paquete_contrato')]

        db_table = 'formas_de_pago'
        ordering = ['id_instrumento']

class Viajeros(models.Model):
    GENERO = {
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    }
    id_de_identidad = models.IntegerField()
    id_ciudad = models.IntegerField()
    id_pais = models.IntegerField()
    id_paquete_contrato = models.ForeignKey(Paquetes_contrato, on_delete=models.CASCADE, related_name='id_paquete_viajeros')
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, null=True, blank=True)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=GENERO)
    f_nacimiento = models.DateField()

    lugar = CompositeForeignKey(Ciudades, on_delete=CASCADE, to_fields={'id': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return str(self.id_de_identidad)

    class Meta:
        db_table = 'viajeros'
        ordering = ['id_de_identidad']

class PAI_VIA(models.Model):
    id_viajero = models.ForeignKey(Viajeros, on_delete=models.CASCADE, related_name='id_viajero_via')
    id_pais = models.ForeignKey(Paices, on_delete=models.CASCADE, related_name='id_pais_via')
    nro_de_pasaporte = models.IntegerField()

    def __str__(self):
        return self.id_viajero + ' ' + self.id_pais

    class Meta:
        db_table = 'paq_via'
        ordering = ['id_viajero']

class Registro_viajeros(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, related_name='id_agencia_reg_via')
    id_viajero = models.ForeignKey(Viajeros, on_delete=models.CASCADE, related_name='id_viajero_reg_via')
    f_registro = models.DateField()
    nro_registro = models.IntegerField()

    def __str__(self):
        return self.id_agencia + ' ' + self.id_viajero

    class Meta:

        unique_together = [('id_viajero', 'id_agencia')]

        db_table = 'registro_viajeros'
        ordering = ['id_viajero']

class Detalle_viajeros(models.Model):
    id_viajero = models.IntegerField()
    id_agencia = models.IntegerField()
    id_paquete_contrato = models.ForeignKey(Paquetes_contrato, on_delete=models.CASCADE, related_name='id_paq_cont_det')

    traveler = CompositeForeignKey(Registro_viajeros, on_delete=CASCADE, to_fields={'id_viajero': 'id_viajero', 'id_agencia': 'id_agencia'})

    def __str__(self):
        return 'v: ' + self.id_viajero + ' a: ' + self.id_agencia + ' ' + self.id_paquete_contrato

    class Meta:

        unique_together = [('id_viajero', 'id_agencia', 'id_paquete_contrato')]

        db_table = 'detalle_viajeros'
        ordering = ['id_viajero']

class Participantes(models.Model):
    id = models.IntegerField(primary_key=True)
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, related_name='id_participantes_rally')
    id_via_agencia = models.IntegerField(null=True, blank=True)
    id_via_viajero = models.IntegerField(null=True, blank=True)
    id_cli_cliente = models.IntegerField(null=True, blank=True)
    id_cli_agencia = models.IntegerField(null=True, blank=True)
    equipo = models.BinaryField(null=True, blank=True)
    posicion = models.IntegerField(null=True, blank=True)

    viajero = CompositeForeignKey(Registro_viajeros, on_delete=CASCADE, to_fields={'id_viajero': 'id_via_viajero', 'id_agencia': 'id_via_agencia'})
    cliente = CompositeForeignKey(Registro_clientes, on_delete=CASCADE, to_fields={'id_cliente': 'id_cli_cliente', 'id_agencia': 'id_cli_agencia'})

    def __str__(self):
        return 'r' + self.id_rally + ' ' + str(self.id)

    class Meta:

        unique_together = [('id_rally', 'id')]

        db_table = 'participantes'
        ordering = ['id']

class Puntuacion(models.Model):
    id = models.IntegerField(primary_key=True)
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, related_name='id_puntuacion_rally', null=True, blank=True)
    id_paquete_contrato = models.ForeignKey(Paquetes_contrato, on_delete=models.CASCADE, related_name='id_paq_cont_puntuacion', null=True, blank=True)
    id_ciudad = models.IntegerField(null=True, blank=True)
    id_pais = models.IntegerField(null=True, blank=True)
    id_atraccion = models.IntegerField(null=True, blank=True)

    lugar = CompositeForeignKey(Atracciones, on_delete=CASCADE, to_fields={'id': 'id_atraccion','id_ciudad': 'id_ciudad', 'id_pais': 'id_pais'})

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'puntuacion'
        ordering = ['id']







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