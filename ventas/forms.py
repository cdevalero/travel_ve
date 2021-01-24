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
