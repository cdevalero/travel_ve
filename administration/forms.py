from django import forms
from django.db.models import fields
from django.forms import DateInput
from .models import *

class Form_Bancos(forms.ModelForm):
    class Meta:
        model = Bancos;
        fields = ('nombre_banco', )

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
        fields = ('nombre_rally', 'costo_participante', 'f_inicio', 'f_fin', 'tipo_rally', 'duracion', 'total_cupo_participante')

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

class Form_Cupos(forms.ModelForm):
    class Meta:
        model = Cupos;
        fields = ('id_agencia','id_rally','cantidad')

class Form_Registro_clientes(forms.ModelForm):
    class Meta:
        model = Registro_clientes;
        fields = ('id_cliente','id_agencia','f_registro','numero_registro')

class Form_Alojamientos(forms.ModelForm):
    class Meta:
        model = Alojamientos;
        fields = ('id_alojamiento','id_ciudad','id_pais','nombre')

class Form_Proveedores(forms.ModelForm):
    class Meta:
        model = Proveedores;
        fields = ('nombre_proveedor','id_proveedor','id_alojamiento','tipo_proveedor')

class Form_PRO_AGE(forms.ModelForm):
    class Meta:
        model = PRO_AGE;
        fields = ('id_agencia','id_proveedor','f_inicio','f_fin')

class Form_Asesores_de_viajes(forms.ModelForm):
    class Meta:
        model = Asesores_de_viajes;
        fields = ('id_asesor','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','telefono')

class Form_Paquetes(forms.ModelForm):
    class Meta:
        model = Paquetes;
        fields = ('id_paquete','id_agencia','nombre_paquete','duracion_dias','descripcion_turistica','disponible','numero_personas')

class Form_Especializaciones(forms.ModelForm):
    class Meta:
        model = Especializaciones;
        fields = ('id_especializacion','id_areas_de_interes','id_atraccion','id_ciudad','id_pais','id_agencia','id_paquete','id_agencia_paquete','id_asesor','comentarios')

class Form_Precios_paquetes(forms.ModelForm):
    class Meta:
        model = Precios_paquetes;
        fields = ('f_inicio','id_paquete','id_agencia','f_fin','valor')

class Form_Calendarios_anuales(forms.ModelForm):
    class Meta:
        model = Calendarios_anuales;
        fields = ('f_salida','id_paquete','id_agencia','descripcion')

class Form_Descuentos(forms.ModelForm):
    class Meta:
        model = Descuentos;
        fields = ('id_descuento','id_agencia','f_inicio','tipo_descuento','f_fin','cant_per_gratis','porcentaje')

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
        fields = ('id_detalle_servicio','id_itinerario','id_paquete','id_agencia','id_ciudad','id_pais','tipo_detalle','descripcion','comida')

class Form_ALO_DET(forms.ModelForm):
    class Meta:
        model = ALO_DET;
        fields = ('id_detalle_servicio','id_itinerario','id_paquete','id_agencia','id_ciudad','id_pais','id_alojamiento')

class Form_Instrumentos_de_pago(forms.ModelForm):
    class Meta:
        model = Instrumentos_de_pago;
        fields = ('id_instrumento','doc_identidad_cliente','monto','tipo_instrumento','id_banco','numero_zelle','email_zelle')

class Form_Paquetes_contrato(forms.ModelForm):
    class Meta:
        model = Paquetes_contrato;
        fields = ('numero_factura','id_paquete','id_agencia','id_reg_cliente','id_reg_agencia','id_asesor','presupuesto','f_aprobacion','f_emision','email_validacion','total_costo_calculado','numer_de_viajeros','f_viaje')

class Form_Formas_de_pago(forms.ModelForm):
    class Meta:
        model = Formas_de_pago;
        fields = ('id_instrumento','id_cliente','id_paquete_contrato','tipo_forma_de_pago')

class Form_Viajeros(forms.ModelForm):
    class Meta:
        model = Viajeros;
        fields = ('id_de_identidad','id_ciudad','id_pais','id_paquete_contrato','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','sexo','f_nacimiento')

class Form_PAI_VIA(forms.ModelForm):
    class Meta:
        model = PAI_VIA;
        fields = ('id_viajero','id_pais','nro_de_pasaporte')

class Form_Registro_viajeros(forms.ModelForm):
    class Meta:
        model = Registro_viajeros;
        fields = ('id_agencia','id_viajero','f_registro','nro_registro')

class Form_Detalle_viajeros(forms.ModelForm):
    class Meta:
        model = Detalle_viajeros;
        fields = ('id_viajero','id_agencia','id_paquete_contrato')

class Form_Participantes(forms.ModelForm):
    class Meta:
        model = Participantes;
        fields = ('id_partipante','id_rally','id_via_agencia','id_via_viajero','id_cli_cliente','id_cli_agencia','equipo','posicion')

class Form_Puntuaciones(forms.ModelForm):
    class Meta:
        model = Puntuaciones;
        fields = ('id_puntuacion','id_rally','id_paquete_contrato','id_ciudad','id_pais','id_atraccion')
