from typing import Tuple
from django.db import models
from django.db.models.deletion import CASCADE
from compositefk.fields import CompositeForeignKey

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






'''
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
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=30)
    tipo_de_operacion = models.CharField(choices=OPERACION, null=False, verbose_name='Tipo de operacion', max_length=1)
    alcance_geografico = models.CharField(choices=ALCANCE, null=False, verbose_name='Alcance geografico', max_length=1)
    web = models.CharField(verbose_name='WEB', null=True, blank = True, max_length=30)
    telefono = models.CharField(verbose_name='Telefono', null=True, blank = True, max_length=30)
    calle_av = models.TextField(verbose_name='Calle/av', null=True, blank = True, max_length=255)
    descripcion = models.TextField(verbose_name='Descripcion', null=True, blank = True, max_length=255)
    id_ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=True, blank = True, related_name='id_ciudad')
    id_pais = models.ForeignKey(Paices, on_delete=models.CASCADE, null=True, blank = True, related_name='id_pais')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'agencias_de_viajes'
        verbose_name = 'Agencia de Viajes'
        verbose_name_plural = 'Agencias de Viajes'
        ordering = ['id']

class AGE_AGE(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia', primary_key=True)
    id_socio = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_socio', primary_key=True)
    f_inicio = models.DateField(verbose_name='Fecha Inicio', null=False)
    f_fin = models.DateField(verbose_name='Fecha Fin', null=True, blank = True)

    def __str__(self):
        return 'Agencia: ' + self.id_agencia + ', ' + 'Socio: ' + self.id_socio


    class Meta:
        db_table = 'age_age'
        verbose_name = 'AGE_AGE'
        verbose_name_plural = 'AGE_AGE'
        ordering = ['id_agencia']

class Cupos(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia', primary_key=True)
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, null=False, related_name='id_rally', primary_key=True)
    cantidad = models.IntegerField(verbose_name='Cantidad', null=True, blank = True)

    def __str__(self):
        return 'Agencia: ' + self.id_agencia + ', ' + 'Rally: ' + self.id_rally


    class Meta:
        db_table = 'cupo'
        verbose_name = 'Cupo'
        verbose_name_plural = 'Cupo'
        ordering = ['id_agencia']

class Registro_clientes(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=False, related_name='id_clientes', primary_key=True)
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia', primary_key=True)
    f_registro = models.DateField(verbose_name='Facha Registro', null=False)
    numero_registro = models.IntegerField(verbose_name='Numero de registro', null=False)

    def __str__(self):
        return 'Cliente: ' + self.id_cliente + ', ' + 'Agencia: ' + self.id_agencia


    class Meta:
        db_table = 'registro_clientes'
        verbose_name = 'Registro de Cliente'
        verbose_name_plural = 'Registro de clientes'
        ordering = ['id_cliente']

class Alojamientos(models.Model):
    id_ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=False, related_name='id_ciudad')
    id_pais = models.ForeignKey(Paices, on_delete=models.CASCADE, null=False, related_name='id_pais')
    nombre = models.IntegerField(verbose_name='Orden', null=True, blank = True, max_length=30)

    def __str__(self):
        return 'Ciudad: ' + self.id_ciudad + ', ' + 'Pais: ' + self.id_pais


    class Meta:
        db_table = 'alojamientos'
        verbose_name = 'Alojamiento'
        verbose_name_plural = 'Alojamientos'
        ordering = ['id']

class Proveedores(models.Model):
    CATEGORIA = (
        ('exclusivo','Exclusivo'),
        ('multiagencias','Multiagencias'),
    )
    id_alojamiento = models.ForeignKey(Alojamientos, on_delete=models.CASCADE, null=False, related_name='id_alojamiento')
    nombre = models.IntegerField(verbose_name='Nombre', null=True, blank = True)
    tipo = models.CharField(max_length=15, choices=CATEGORIA, null=False, verbose_name='Tipo')

    def __str__(self):
        return self.nombre


    class Meta:
        db_table = 'proveedores'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['id']

class PRO_AGE(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia', primary_key=True)
    id_proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, null=False, related_name='id_proveedor', primary_key=True)
    f_inicio = models.DateField(verbose_name='Fecha Inicio', null=False)
    f_fin = models.DateField(verbose_name='Fecha Fin', null=True, blank = True)

    def __str__(self):
        return 'Agencia: ' + self.id_agencia + ', ' + 'Proveedor: ' + self.id_proveedor


    class Meta:
        db_table = 'pro_age'
        verbose_name = 'PRO_AGE'
        verbose_name_plural = 'PRO_AGE'
        ordering = ['id']

class Asesores_de_viajes(models.Model):
    primer_nombre = models.CharField(verbose_name='Primer nombre', null=False, max_length=30)
    segundo_nombre = models.CharField(verbose_name='Segundo apellido', null=True, blank=True, max_length=30)
    primer_apellido = models.CharField(verbose_name='Primer apellido', null=False, max_length=30)
    segundo_apellido = models.CharField(verbose_name='Segundo apellido', null=False, max_length=30)
    telefono = models.IntegerField(verbose_name='Telefono', null=False)

    def __str__(self):
        return self.primer_apellido + ', ' + self.primer_nombre


    class Meta:
        db_table = 'asesores_de_viajes'
        verbose_name = 'Asesor de viaje'
        verbose_name_plural = 'Asesores de viaje'
        ordering = ['id']

class Paquetes(models.Model):
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia', primary_key=True)
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=30)
    duracion_en_dias = models.IntegerField(null=False, verbose_name='Duracion en dias')
    descripcion_turistica = models.TextField(verbose_name='Descripcion turistica', null=False, max_length=255)
    disponible = models.BooleanField(verbose_name='Disponible', null=True, blank=True)
    numero_de_personas = models.IntegerField(verbose_name='Numero de personas', null=True, blank=True)

    def __str__(self):
        return self.nombre


    class Meta:
        db_table = 'paquetes'
        verbose_name = 'Paquete'
        verbose_name_plural = 'Paquetes'
        ordering = ['id']

class Especializaciones(models.Model):
    id_area = models.ForeignKey(Areas_de_interes, on_delete=models.CASCADE, null=False, related_name='id_area', primary_key=True)
    id_atraccion = models.ForeignKey(Atracciones, on_delete=models.CASCADE, null=False, related_name='id_atraccion')
    id_ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=False, related_name='id_ciudad')
    id_pais = models.ForeignKey(Paices, on_delete=models.CASCADE, null=False, related_name='id_pais')
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia')
    id_paquete = models.ForeignKey(Paquetes, on_delete=models.CASCADE, null=False, related_name='id_paquete')
    id_agencia_paquete = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia_paquete')
    id_asesor = models.ForeignKey(Asesores_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_asesor')
    comentarios = models.TextField(null=False, verbose_name='Comentarios', max_length=255)

    def __str__(self):
        return self.id_area


    class Meta:
        db_table = 'especializaciones'
        verbose_name = 'Especializacion'
        verbose_name_plural = 'Especializaciones'
        ordering = ['id']

class Precio_paquetes(models.Model):
    f_inicio = models.DateField(verbose_name='Fecha Inicio', null=False, primary_key=True)
    id_paquete = models.ForeignKey(Paquetes, on_delete=models.CASCADE, null=False, related_name='id_paquete', primary_key=True)
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia', primary_key=True)
    f_fin = models.DateField(verbose_name='Fecha fin', null=True, blank=True)
    valor = models.IntegerField(verbose_name='Valor', null=True, blank=True)

    def __str__(self):
        return self.f_inicio + '-' + self.id_paquete + '-' + self.id_agencia


    class Meta:
        db_table = 'precio_paquetes'
        verbose_name = 'Precio de paquete'
        verbose_name_plural = 'Precio de paquetes'
        ordering = ['f_inicio']

class Calendarios_anuales(models.Model):
    f_salida = models.DateField(verbose_name='Fecha Salida', null=False, primary_key=True)
    id_paquete = models.ForeignKey(Paquetes, on_delete=models.CASCADE, null=False, related_name='id_paquete', primary_key=True)
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia', primary_key=True)
    descripcion = models.TextField(verbose_name='Descripcion', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.f_salida + '-' + self.id_paquete + '-' + self.id_agencia


    class Meta:
        db_table = 'calendarios_anuales'
        verbose_name = 'Calendario anual'
        verbose_name_plural = 'Calendarios anuales'
        ordering = ['f_salida']

class Descuentos(models.Model):
    DESCUENTO = (
        ('descnino','Descuento niño'),
        ('adultos','Adultos'),
        ('general','General'),
        ('viajerosgratis','Viaje gratis'),
        ('otro','Otro'),
    )
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia', primary_key=True)
    f_inicio = models.DateField(verbose_name='Fecha Inicio', null=False)
    tipo = models.CharField(max_length=20, choices=DESCUENTO, null=False, verbose_name='Tipo')
    f_fin = models.DateField(verbose_name='Fecha Fin', null=True, blank=True)
    cant_per_gratis = models.IntegerField(verbose_name='Cantidad de personas gratis', null=True, blank=True)
    porcentaje = models.IntegerField(verbose_name='%', null=True, blank=True)

    def __str__(self):
        return self.id_agencia

    class Meta:
        db_table = 'descuentos'
        verbose_name = 'Descuento'
        verbose_name_plural = 'Descuentos'
        ordering = ['id']

class Intinerarios(models.Model):
    orden = models.IntegerField(verbose_name='Orden', primary_key=True, null=False)
    id_ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=False, related_name='id_ciudad', primary_key=True)
    id_pais = models.ForeignKey(Paices, on_delete=models.CASCADE, null=False, related_name='id_pais', primary_key=True)
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia', primary_key=True)
    id_paquete = models.ForeignKey(Paquetes, on_delete=models.CASCADE, null=False, related_name='id_paquete', primary_key=True)
    tiempo_estadia = models.IntegerField(verbose_name='Tiempo de estadia', null=False)

    def __str__(self):
        return str(self.orden) + '- ' + self.id_paquete + '-' + self.id_agencia + ' ' + self.id_ciudad + ', ' + self.id_pais


    class Meta:
        db_table = 'intinerarios'
        verbose_name = 'Intinerario'
        verbose_name_plural = 'Intinerarios'
        ordering = ['orden']

class INT_ATR(models.Model):
    id_intinerario = models.ForeignKey(Intinerarios, on_delete=models.CASCADE, null=False, related_name='id_intinerario', primary_key=True)
    id_atraccion = models.ForeignKey(Atracciones, on_delete=models.CASCADE, null=False, related_name='id_atraccion', primary_key=True)
    id_ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=False, related_name='id_ciudad', primary_key=True)
    id_pais = models.ForeignKey(Paices, on_delete=models.CASCADE, null=False, related_name='id_pais', primary_key=True)
    id_agencia = models.ForeignKey(Agencias_de_viajes, on_delete=models.CASCADE, null=False, related_name='id_agencia', primary_key=True)
    id_paquete = models.ForeignKey(Paquetes, on_delete=models.CASCADE, null=False, related_name='id_paquete', primary_key=True)
    orden_visita = models.IntegerField(verbose_name='Tiempo de visita', null=False)

    def __str__(self):
        return  self.id_intinerario + ' -> ' + self.id_atraccion

    class Meta:
        db_table = 'INT_ATR'
        verbose_name = 'INT_ATR'
        verbose_name_plural = 'INT_ATR'
        ordering = ['id_intinerario']
'''