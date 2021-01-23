from django import forms
from django.db.models import fields
from django.forms import DateInput
from django.forms.models import ModelChoiceField
from django.forms.widgets import Textarea
from .models import *

class Form_Bancos(forms.ModelForm):
    class Meta:
        model = Bancos;
        fields = ('nombre_banco',)

class Form_Clientes(forms.ModelForm):
    class Meta:
        model = Clientes;
        fields = ('doc_identidad_o_rif', 'nombre_cliente', 'primer_apellido', 'segundo_apellido', 'tipo_cliente')

class Form_Areas_de_interes(forms.ModelForm):
    class Meta:
        model = Areas_de_interes;
        fields = ('nombre_area_de_interes', 'descripcion_area_de_interes')

class Form_Paises(forms.ModelForm):
    class Meta:
        model = Paises;
        fields = ('nombre_pais', 'region_pais', 'continente_pais', 'nacionalidad', 'descripcion_pais')

class Form_Rallies(forms.ModelForm):
    class Meta:
        model = Rallies;
        fields = ('nombre_rally', 'costo_participante', 'f_inicio', 'f_fin', 'tipo_rally', 'total_cupo_participante')
        widgets = {
            'f_inicio': DateInput(attrs={'type': 'date'}),
            'f_fin': DateInput(attrs={'type': 'date'})
        }

class Form_Premios(forms.ModelForm):
    class Meta:
        model = Premios;
        fields = ('id_rally', 'posicion', 'descripcion_premio')

class Form_Ciudades(forms.ModelForm):
    class Meta:
        model = Ciudades;
        fields = ('id_pais','nombre_ciudad', 'tipo_ciudad', 'descripcion_ciudad')

class Form_Atracciones(forms.ModelForm):
    class Meta:
        model = Atracciones;
        fields = ( 'id_ciudad', 'id_pais','nombre_atraccion', 'descripcion_atraccion')

class Form_Circuitos(forms.ModelForm):
    class Meta:
        model = Circuitos;
        fields = ('orden_circuito','id_rally','id_ciudad', 'id_pais', 'maxdias')

class Form_ATR_CIR(forms.ModelForm):
    class Meta:
        model = ATR_CIR;
        fields = ('id_atraccion','id_ciudad_at','id_pais_at', 'id_circuito', 'id_rally_cir','id_ciudad_cir','id_pais_cir','orden')

class Form_Agencia_de_viajes(forms.ModelForm):
    class Meta:
        model = Agencias_de_viajes;
        fields = ('nombre','tipo_de_operacion', 'alcance_geografico', 'web','telefono','calle_av','descripcion','id_ciudad','id_pais')

class Form_AGE_AGE(forms.ModelForm):
    class Meta:
        model = AGE_AGE;
        fields = ('id_agencia','id_socio','f_inicio', 'f_fin')
        widgets = {
            'f_inicio': DateInput(attrs={'type': 'date'}),
            'f_fin': DateInput(attrs={'type': 'date'})
        }

class Form_Cupos(forms.ModelForm):
    class Meta:
        model = Cupos;
        fields = ('id_agencia','id_rally','cantidad')

class Form_Registro_clientes(forms.ModelForm):
    class Meta:
        model = Registro_clientes;
        fields = ('id_cliente','id_agencia','f_registro')
        widgets = {
            'f_registro': DateInput(attrs={'type': 'date'})
        }

class Form_Alojamientos(forms.ModelForm):
    class Meta:
        model = Alojamientos;
        fields = ('id_ciudad','id_pais','nombre')

class Form_Proveedores(forms.ModelForm):
    class Meta:
        model = Proveedores;
        fields = ('nombre_proveedor','id_alojamiento','tipo_proveedor')

class Form_PRO_AGE(forms.ModelForm):
    class Meta:
        model = PRO_AGE;
        fields = ('id_agencia','id_proveedor','f_inicio','f_fin')
        widgets = {
            'f_inicio': DateInput(attrs={'type': 'date'}),
            'f_fin': DateInput(attrs={'type': 'date'})
        }

class Form_Asesores_de_viajes(forms.ModelForm):
    class Meta:
        model = Asesores_de_viajes;
        fields = ('primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','telefono')

class Form_Paquetes(forms.ModelForm):
    class Meta:
        model = Paquetes;
        fields = ('id_paquete','id_agencia','nombre_paquete','duracion_dias','descripcion_turistica','disponible','numero_personas')

class Form_Especializaciones(forms.ModelForm):
    class Meta:
        model = Especializaciones;
        fields = ('id_areas_de_interes','id_atraccion','id_ciudad','id_pais','id_agencia','id_paquete','id_agencia_paquete','id_asesor','comentarios')

class Form_Precios_paquetes(forms.ModelForm):
    class Meta:
        model = Precios_paquetes;
        fields = ('f_inicio','f_fin','id_paquete','id_agencia','valor')
        widgets = {
            'f_inicio': DateInput(attrs={'type': 'date'}),
            'f_fin': DateInput(attrs={'type': 'date'})
        }

class Form_Calendarios_anuales(forms.ModelForm):
    class Meta:
        model = Calendarios_anuales;
        fields = ('f_salida','id_paquete','id_agencia','descripcion')
        widgets = {
            'f_salida': DateInput(attrs={'type': 'date'})
        }

class Form_Descuentos(forms.ModelForm):
    class Meta:
        model = Descuentos;
        fields = ('id_agencia','f_inicio','tipo_descuento','f_fin','cant_per_gratis','porcentaje')
        widgets = {
            'f_inicio': DateInput(attrs={'type': 'date'}),
            'f_fin': DateInput(attrs={'type': 'date'})
        }

class Form_Itinerarios(forms.ModelForm):
    class Meta:
        model = Itinerarios;
        fields = ('orden','id_ciudad','id_pais','id_agencia','id_paquete','tiempo_estadia')

class Form_ITN_ATR(forms.ModelForm):
    class Meta:
        model = ITN_ATR;
        fields = ('id_itinerario','id_ciudad','id_pais','id_agencia','id_paquete','id_atraccion','id_ciudad_at','id_pais_at','orden_visita')

class Form_Detalles_servicios(forms.ModelForm):
    class Meta:
        model = Detalles_servicios;
        fields = ('id_itinerario','id_paquete','id_agencia','id_ciudad','id_pais','tipo_detalle','descripcion','comida')

class Form_ALO_DET(forms.ModelForm):
    class Meta:
        model = ALO_DET;
        fields = ('id_detalle_servicio','id_itinerario','id_paquete','id_agencia','id_ciudad','id_pais','id_alojamiento')

class Form_Instrumentos_de_pago(forms.ModelForm):
    class Meta:
        model = Instrumentos_de_pago;
        fields = ('doc_identidad_cliente','monto','tipo_instrumento','id_banco','numero_zelle','email_zelle')

class Form_Paquetes_contrato(forms.ModelForm):
    class Meta:
        model = Paquetes_contrato;
        fields = ('id_paquete','id_agencia','id_reg_cliente','id_reg_agencia','id_asesor','presupuesto','f_aprobacion','f_emision','email_validacion','total_costo_calculado','numer_de_viajeros','f_viaje')
        widgets = {
            'f_aprobacion': DateInput(attrs={'type': 'date'}),
            'f_emision': DateInput(attrs={'type': 'date'}),
            'f_viaje': DateInput(attrs={'type': 'date'})
        }

class Form_Formas_de_pago(forms.ModelForm):
    class Meta:
        model = Formas_de_pago;
        fields = ('id_instrumento','id_cliente','id_paquete_contrato','tipo_forma_de_pago')

class Form_Viajeros(forms.ModelForm):
    class Meta:
        model = Viajeros;
        fields = ('id_de_identidad','id_ciudad','id_pais','id_paquete_contrato','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','sexo','f_nacimiento')
        widgets = {
            'f_nacimiento': DateInput(attrs={'type': 'date'})
        }

class Form_PAI_VIA(forms.ModelForm):
    class Meta:
        model = PAI_VIA;
        fields = ('id_viajero','id_pais','nro_de_pasaporte')

class Form_Registro_viajeros(forms.ModelForm):
    class Meta:
        model = Registro_viajeros;
        fields = ('id_agencia','id_viajero','f_registro','nro_registro')
        widgets = {
            'f_registro': DateInput(attrs={'type': 'date'})
        }

class Form_Detalle_viajeros(forms.ModelForm):
    class Meta:
        model = Detalle_viajeros;
        fields = ('id_viajero','id_agencia','id_paquete_contrato')

class Form_Participantes(forms.ModelForm):
    class Meta:
        model = Participantes;
        fields = ('id_rally','id_via_agencia','id_via_viajero','id_cli_cliente','id_cli_agencia','equipo','posicion')

class Form_Puntuaciones(forms.ModelForm):
    class Meta:
        model = Puntuaciones;
        fields = ('id_rally','id_paquete_contrato','id_ciudad','id_pais','id_atraccion')

class Form_nuevo_registro_cliente(forms.Form):
    PERSONA = (
        ('natural','Natural'),
        ('juridico','Juridico'),
    )
    tipo = forms.ChoiceField(choices=PERSONA, label='Tipo')
    cedula = forms.IntegerField(label='Documento de Identidad / RIF')
    nombre = forms.CharField(label='Nombres', max_length=30)
    apellido1 = forms.CharField(label='Primer Apellido', max_length=30, required=False)
    apellido2 = forms.CharField(label='Segundo Apellido', max_length=30, required=False)
    agencia = ModelChoiceField(Agencias_de_viajes.objects.all(), label='Agencia de Viajes')

class Form_nuevo_registro_viajero(forms.Form):
    GENERO = {
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    }
    cedula = forms.IntegerField(label='Documento de Identidad')
    nombre1 = forms.CharField(label='Primer nombre nombre', max_length=30)
    nombre2 = forms.CharField(label='Segundo nombre', max_length=30, required=False)
    apellido1 = forms.CharField(label='Primer Apellido', max_length=30)
    apellido2 = forms.CharField(label='Segundo Apellido', max_length=30)
    sexo = forms.ChoiceField(choices=GENERO, label='Sexo')
    f_nacimento = forms.DateField(label='Fecha de nacimeinto', widget=DateInput(attrs={'type': 'date'}))
    ciudad = ModelChoiceField(Ciudades.objects.all(), label='Ciudad donde recide')
    pasaporte = forms.IntegerField(label='Pasaporte')
    pais = ModelChoiceField(Paises.objects.all(), label='Nacionalidad')
    f_registro = forms.DateField(label='Fecha de registro',  widget=DateInput(attrs={'type': 'date'}))
    paquete = ModelChoiceField(Paquetes_contrato.objects.all(), label='Paquete contrato')

class Form_nuevo_socio_proveedor(forms.Form):
    CATEGORIA = (
        ('exclusivo','Exclusivo'),
        ('multiagencias','Multiagencias'),
    )
    nombre = forms.CharField(label='Nombre de Proveedor', max_length=30)
    tipo = forms.ChoiceField(choices=CATEGORIA, label='Tipo de Proveedor')
    alojamiento = ModelChoiceField(Alojamientos.objects.all(), label='Alojamiento')
    agencia = ModelChoiceField(Agencias_de_viajes.objects.all(), label='Agencia de Viajes')
    f_inicio = forms.DateField(label='Inicio de asociacion', widget=DateInput(attrs={'type': 'date'}))
    f_fin = forms.DateField(label='Fin de asociacion', required=False, widget=DateInput(attrs={'type': 'date'}))




class Form_nuevo_paquete_basico(forms.Form):
    agencia = ModelChoiceField(Agencias_de_viajes.objects.all(), label='Agencia de Viajes')
    nombre = forms.CharField(label='Nombre del paquete', max_length=30)
    Duracion = forms.IntegerField(label='Duracion (en dias)')
    personas = forms.IntegerField(label='Numero de personas')
    descripcion = forms.CharField(label='Descripcion', max_length=255, widget=Textarea())
    disponible = forms.BooleanField(label='Disponible', required=False)

class Form_nuevo_paquete_itinerario(forms.Form):
    orden = forms.IntegerField(label='Orden')
    ciudad = ModelChoiceField(Ciudades.objects.all(), label='Ciudad')
    max = forms.IntegerField(label='Tiempo de estadia (tiempo MAXIMO que puedes pasar en este tramo)')
    tiempo = forms.IntegerField(label='Tiempo de estadia (Menor o igual al tiempo maximo) *Si es 0, Se termina el itinerario')
    paquete = forms.IntegerField(label='')
    agencia = forms.IntegerField(label='')

class Form_nuevo_paquete_itn_atr(forms.Form):
    orden = forms.IntegerField(label='Orden')
    atraccion = forms.ModelChoiceField(Atracciones.objects.all(), label='Atraccion (Si no se escoge ninguna, la entrada no se guardara)', required=False)
    itn = forms.IntegerField(label='Itinerario')
    ciudad = forms.IntegerField(label='')
    pais = forms.IntegerField(label='')
    agencia = forms.IntegerField(label='')
    paquete = forms.IntegerField(label='')
    max = forms.IntegerField(label='')
    def __init__(self, ciudad, *args, **kwargs):
        super(Form_nuevo_paquete_itn_atr, self).__init__(*args, **kwargs)
        self.fields['atraccion'].queryset = Atracciones.objects.filter(id_ciudad=ciudad)

class Form_nuevo_paquete_itn_atr_post(forms.Form):
    orden = forms.IntegerField(label='Orden')
    atraccion = forms.ModelChoiceField(Atracciones.objects.all(), label='Atraccion')
    itn = forms.IntegerField(label='Itinerario')
    ciudad = forms.IntegerField(label='Ciudad')
    pais = forms.IntegerField(label='Pais')
    agencia = forms.IntegerField(label='Agencia')
    paquete = forms.IntegerField(label='Paquete')
    max = forms.IntegerField(label='Tiempo restante de viaje')
   
class Form_nuevo_paquete_det_ser(forms.Form):
    BOLETO = {
        ('boleto_avion', 'Boleto de avion'),
        ('boleto_tren', 'Boleto de tren'),
        ('boleto_autobus', 'Boleto de Autobus'),
        ('cama_alq', 'Cama de alquiler'),
        ('alojamiento', 'Alojamiento'),
        ('otro', 'otros'),
        ('-----', '-----'),
    }
    itinerario = forms.IntegerField(label='Itinerario')
    tipo = forms.ChoiceField(choices=BOLETO, label='Tipo')
    descripcion = forms.CharField(label='Descripcion', max_length=255, widget=Textarea())
    comida = forms.BooleanField(label='Incluye Comida', required=False)
    paquete = forms.IntegerField(label='')
    agencia = forms.IntegerField(label='')
    ciudad = forms.IntegerField(label='')
    pais = forms.IntegerField(label='')
    max = forms.IntegerField(label='')
    
class Form_nuevo_paquete_alo_det(forms.Form):
    detalle = forms.IntegerField(label='')
    alojamiento = forms.ModelChoiceField(Alojamientos.objects.all(), label='Alojamiento', required=False)
    itn = forms.IntegerField(label='')
    paquete = forms.IntegerField(label='')
    agencia = forms.IntegerField(label='')
    ciudad = forms.IntegerField(label='')
    pais = forms.IntegerField(label='')
    max = forms.IntegerField(label='')
    def __init__(self, ciudad, *args, **kwargs):
        super(Form_nuevo_paquete_alo_det, self).__init__(*args, **kwargs)
        self.fields['alojamiento'].queryset = Alojamientos.objects.filter(id_ciudad=ciudad)

class Form_nuevo_paquete_alo_det_post(forms.Form):
    detalle = forms.IntegerField(label='')
    alojamiento = forms.ModelChoiceField(Alojamientos.objects.all(), label='Alojamiento', required=False)
    itn = forms.IntegerField(label='')
    paquete = forms.IntegerField(label='')
    agencia = forms.IntegerField(label='')
    ciudad = forms.IntegerField(label='')
    pais = forms.IntegerField(label='')
    max = forms.IntegerField(label='')

class Form_nuevo_paquete_calendario(forms.Form):
    salida = forms.DateField(label='Fecha de salidad', widget=DateInput(attrs={'type': 'date'}))
    paquete = forms.IntegerField(label='')
    agencia = forms.IntegerField(label='')
    descripcion = forms.CharField(label='Descripcion', max_length=255, widget=Textarea()) 

class Form_nuevo_paquete_precio(forms.Form):
    inicio = forms.DateField(label='Fecha Inicio', widget=DateInput(attrs={'type': 'date'}))
    fin = forms.DateField(label='Fecha Fin', required=False , widget=DateInput(attrs={'type': 'date'}))
    valor = forms.IntegerField(label='Valor')
    paquete = forms.IntegerField(label='')
    agencia = forms.IntegerField(label='')
    