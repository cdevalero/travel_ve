from typing import Tuple
from django.db import models

class Bancos(models.Model):
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'bancos'
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
        ordering = ['id']

class Clientes(models.Model):
    PERSONA = (
        ('natural','Natural'),
        ('juridico','Juridico'),
    )
    doc_identidad_rif = models.IntegerField(primary_key=True, verbose_name='Doc Identidad o RIF', null=False)
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=30)
    tipo = models.CharField(max_length=10, choices=PERSONA, null=False, verbose_name='Tipo')

    def __str__(self):
        return str(self.doc_identidad_rif)

    class Meta:
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['doc_identidad_rif']

class Areas_de_interes(models.Model):
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=30, unique=True)
    descripcion = models.TextField(verbose_name='Descripción', null=False, max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'areas_de_interes'
        verbose_name = 'Area de interes'
        verbose_name_plural = 'Areas de interes'
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
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=30)
    region = models.CharField(max_length=15, choices=REGIONES, null=False, verbose_name='Región')
    continente = models.CharField(max_length=15, choices=CONTINENTES, null=False, verbose_name='Continentes')
    nacionalidad = models.CharField(null=False, verbose_name='Nacionalidad', max_length=60)
    descripcion = models.TextField(verbose_name='Descripción', null=False, max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'paices'
        verbose_name = 'Pais'
        verbose_name_plural = 'Paices'
        ordering = ['id']

class Rallies(models.Model):
    CATEGORIA = (
        ('individual','Individual'),
        ('pareja','Pareja'),
    )
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=30)
    costo_participante = models.IntegerField(verbose_name='Costo por Participante', null=False)
    f_inicio = models.DateField(verbose_name='Fecha Inicio', null=False)
    f_fin = models.DateField(verbose_name='Fecha Fin', null=False)
    tipo = models.CharField(max_length=15, choices=CATEGORIA, null=False, verbose_name='Tipo')
    duracion = models.IntegerField(null=False, verbose_name='Duracion')
    total_cupo_participante = models.IntegerField(verbose_name='Total cupo por participante', null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'rallies'
        verbose_name = 'Rally'
        verbose_name_plural = 'Rallies'
        ordering = ['id']

class Premios(models.Model):
    PREMIO = (
        (1,'1er'),
        (2,'2do'),
        (3,'3ro'),
    )
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, null=False, related_name='id_rally', primary_key=True)
    posicion = models.IntegerChoices(choices=PREMIO, null=False, verbose_name='Posicion')
    descripcion = models.TextField(verbose_name='Descripción', null=False, max_length=255)

    def __str__(self):
        return 'Rally: ' + self.id_rally + ', ' + 'Posicion: ' + str(self.posicion)

    class Meta:
        db_table = 'premios'
        verbose_name = 'Premio'
        verbose_name_plural = 'Premios'
        ordering = ['id']

class Ciudades(models.Model):
    DESTINO = (
        ('localidad','Localidad'),
        ('ciudad','Ciudad'),
    )
    id_pais = models.ForeignKey(Paices, on_delete=models.CASCADE, null=False, related_name='id_pais', primary_key=True)
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=30)
    tipo = models.CharField(choices=DESTINO, null=False, verbose_name='tipo', max_length=15)
    descripcion = models.TextField(verbose_name='Descripción', null=False, max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'ciudades'
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['id']

class Atracciones(models.Model):
    id_ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=False, related_name='id_ciudad', primary_key=True)
    id_pais = models.ForeignKey(Paices, on_delete=models.CASCADE, null=False, related_name='id_pais', primary_key=True)
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=30)
    descripcion = models.TextField(verbose_name='Descripción', null=False, max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'atracciones'
        verbose_name = 'Atraccion'
        verbose_name_plural = 'Atracciones'
        ordering = ['id']

class Circuitos(models.Model):
    orden = models.IntegerField(primary_key=True, verbose_name='Orden', null=False)
    id_ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=False, related_name='id_ciudad', primary_key=True)
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, null=False, related_name='id_rally', primary_key=True)
    id_pais = models.ForeignKey(Paices, on_delete=models.CASCADE, null=False, related_name='id_pais', primary_key=True)
    nombre = models.CharField(null=False, verbose_name='Nombre', max_length=30)
    descripcion = models.TextField(verbose_name='Descripción', null=False, max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'circuitos'
        verbose_name = 'Circuito'
        verbose_name_plural = 'Circuitos'
        ordering = ['orden']

class ART_CIR(models.Model):
    id_atraccion = models.ForeignKey(Atracciones, on_delete=models.CASCADE, null=False, related_name='id_atraccion', primary_key=True)
    id_ciudad_at = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=False, related_name='id_ciudad atraccion', primary_key=True)
    id_pais_at = models.ForeignKey(Paices, on_delete=models.CASCADE, null=False, related_name='id_pais atraccion', primary_key=True)
    id_circuito = models.ForeignKey(Circuitos, on_delete=models.CASCADE, null=False, related_name='id_circuito', primary_key=True)
    id_rally_cir = models.ForeignKey(Rallies, on_delete=models.CASCADE, null=False, related_name='id_rally circuito', primary_key=True)
    id_ciudad_cir = models.ForeignKey(Ciudades, on_delete=models.CASCADE, null=False, related_name='id_ciudad circuito', primary_key=True)
    id_pais_cir = models.ForeignKey(Paices, on_delete=models.CASCADE, null=False, related_name='id_pais circuito', primary_key=True)
    orden = models.IntegerField(verbose_name='Orden', null=True, blank = True)

    def __str__(self):
        return 'Atraccion: ' + self.id_atraccion + ', ' + 'Circuito: ' + self.id_circuito


    class Meta:
        db_table = 'art_cir'
        verbose_name = 'ART_CIR'
        verbose_name_plural = 'ART_CIR'
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
        ('exclusivo','Exclusivo')
        ('multiagencias','Multiagencias')
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