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
        return self.doc_identidad_rif

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
    id_rally = models.ForeignKey(Rallies, on_delete=models.CASCADE, null=False, related_name='id_rally' primary_key=True)
    posicion = models.IntegerChoices(choices=PREMIO, null=False, verbose_name='Posicion')
    descripcion = models.TextField(verbose_name='Descripción', null=False, max_length=255)

    def __str__(self):
        return 'Rally: ' + str(self.id_rally) + ', ' + 'Posicion: ' + str(self.posicion)

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
        return 'Atraccion: ' + str(self.id_atraccion) + ', ' + 'Circuito: ' + str(self.id_circuito)
        return self.nombre + ' ' + self.apellido1 + ' ' + self.apellido2

    class Meta:
        db_table = 'art_cir'
        verbose_name = 'ART_CIR'
        verbose_name_plural = 'ART_CIR'
        ordering = ['id_atraccion']

