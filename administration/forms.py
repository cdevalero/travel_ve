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
        fields = ('nombre_ciudad', 'id_pais', 'tipo_ciudad', 'descripcion_ciudad')

class Form_Atracciones(forms.ModelForm):
    class Meta:
        model = Atracciones;
        fields = ('nombre_atraccion', 'id_ciudad', 'id_pais', 'descripcion_atraccion')









