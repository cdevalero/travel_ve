from django import forms
from django.forms import DateInput
from django.forms.models import ModelChoiceField
from administration.models import Agencias_de_viajes

class Form_nuevo_registro_cliente(forms.Form):
    PERSONA = (
        ('natural','Natural'),
        ('juridico','Juridico'),
    )
    tipo = forms.ChoiceField(choices=PERSONA, label='Tipo')
    cedula = forms.IntegerField(label='Documento de Identidad / RIF')
    nombre = forms.CharField(label='Nombres', max_length=30)
    apellido1 = forms.CharField(label='Primer Apellido', max_length=30)
    apellido2 = forms.CharField(label='Segundo Apellido', max_length=30)
    agencia = ModelChoiceField(Agencias_de_viajes.objects.all(), label='Agencia de Viajes')
    numero = forms.IntegerField(label='Numero de registro')