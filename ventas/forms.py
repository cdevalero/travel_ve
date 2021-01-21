from django import forms
from django.forms import DateInput
from django.forms.models import ModelChoiceField
from django.forms.widgets import SplitDateTimeWidget
from administration.models import *
from django.contrib.admin.widgets import AdminDateWidget

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

class Form_Ventas_Instrumentos_pago(forms.Form):
    class Meta:
        model = Instrumentos_de_pago;
        fields = ('doc_identidad_cliente','monto','tipo_instrumento','id_banco','numero_zelle','email_zelle')

class Form_nuevo_registro_viajero(forms.Form):
    GENERO = {
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    }
    cedula = forms.IntegerField(label='Documento de Identidad')
    nombre1 = forms.CharField(label='Primer nombre', max_length=30)
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

    