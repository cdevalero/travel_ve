from django import forms
from django.db.models import fields
from django.forms import DateInput
from django.forms.models import ModelChoiceField
from django.forms.widgets import Textarea
from administration.models import *

class Form_Buscar_paquerte(forms.Form):
    agencia = ModelChoiceField(Agencias_de_viajes.objects.all(), label='Agencia de Viajes', required=False)
    ciudad = ModelChoiceField(Ciudades.objects.all(), label='Ciudades', required=False)
    personas = forms.IntegerField(label='Nro Personas', required=False)
    fecha = forms.DateField(label='Fecha Aproximada', required=False , widget=DateInput(attrs={'type': 'date'}))
    area = ModelChoiceField(Areas_de_interes.objects.all(), label='Area de interes', required=False)

class Form_Seleccionar_agente(forms.Form):
    PERSONA = (
        ('natural','Natural'),
        ('juridico','Juridico'),
    )
    agente = ModelChoiceField(Asesores_de_viajes.objects.all(), label='Asesor de Viajes', required=False, help_text='Si lo desea puede escoger un asesor para planificar el viaje')
    cliente = forms.IntegerField(label='identificacion del Cliente')
    tipo = forms.ChoiceField(choices=PERSONA, label='Tipo de cliente')
    nombre = forms.CharField(label='Nombre del Cliente')
    apellido1 = forms.CharField(label='Apellido 1', required=False)
    apellido2 = forms.CharField(label='Apellido 2', required=False)

class Form_ventas_buscar_paquete(forms.Form):
    agencia = ModelChoiceField(Agencias_de_viajes.objects.all(), label='Agencia de Viajes', required=False)
    ciudad = ModelChoiceField(Ciudades.objects.all(), label='Ciudades', required=False)
    personas = forms.IntegerField(label='Nro Personas', required=False)
    agente = forms.IntegerField(label='')
    cliente = forms.IntegerField(label='')
    fecha = forms.DateField(label='Fecha Aproximada', required=False , widget=DateInput(attrs={'type': 'date'}))
    area = ModelChoiceField(Areas_de_interes.objects.all(), label='Area de interes', required=False)

class Form_ventas_descuneto_forma(forms.Form):
    TRAMITES = {
        ('parcial', 'Parcial'),
        ('cuotas', 'Cuotas'),
    }
    tipo = forms.ChoiceField(choices=TRAMITES, label='Forma de pago')
    descuento =  ModelChoiceField(Descuentos.objects.all(), label='Descuentos disponibles', required=False)
    email = forms.EmailField(label='Email de conctacto cliente')
    def __init__(self, agencia, fecha, *args, **kwargs):
        super(Form_ventas_descuneto_forma, self).__init__(*args, **kwargs)
        self.fields['descuento'].queryset = Descuentos.objects.filter(id_agencia=agencia, f_fin__range=(fecha, "2099-01-31")) | Descuentos.objects.filter(id_agencia=agencia, f_fin=None)

class Form_ventas_descuneto_forma_post(forms.Form):
    TRAMITES = {
        ('parcial', 'Parcial'),
        ('cuotas', 'Cuotas'),
    }
    tipo = forms.ChoiceField(choices=TRAMITES, label='Forma de pago')
    descuento =  ModelChoiceField(Descuentos.objects.all(), label='Descuentos disponibles', required=False)

class Form_ventas_instrumento(forms.Form):
    INSTRUMENTO = {
        ('TDC', 'Tarjeta de Credito'),
        ('TDD', 'Tarjeta de Debito'),
        ('ctabanco', 'Cuanta Bancaria'),
        ('zelle', 'Zelle'),
    }
    max= forms.IntegerField(label='Deuda a pagar')
    monto = forms.IntegerField(label='Monto', help_text='Debe ser igual a la deuda, si es menor se agregara otro instrumento de pago')
    tipo = forms.ChoiceField(choices=INSTRUMENTO, label='Tipo de Pago')
    banco =  ModelChoiceField(Bancos.objects.all(), label='Banco', required=False, help_text='No usar en caso de pago Zelle')
    numero = forms.IntegerField(label='Numero Zelle', help_text='Solo pago Zelle', required=False)
    email = forms.EmailField(label='Email Zelle', help_text='Solo pago Zelle', required=False)


