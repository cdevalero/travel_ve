from administration.sql_functions import Crear_PAI_VIA, Crear_Registro_viajeros
from administration.forms import Form_Instrumentos_de_pago
from django.db import connection
from administration.models import Agencias_de_viajes, Ciudades, Paises, Paquetes, Paquetes_contrato
from django.http.response import HttpResponse
from ventas.forms import Form_nuevo_registro_cliente, Form_nuevo_registro_viajero
from django.shortcuts import redirect, render
from datetime import date
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

# SQL ----------------------------------------------------------------------------------------------------

def Crear_nuevo_Registro_clientes(cliente, agencia, fecha):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_registro_clientes(id_cliente, id_agencia, f_registro, numero_registro) VALUES (%s, %s, %s, (SELECT max(r.numero_registro) from cgr_registro_clientes r) + 1)', 
        [cliente, agencia, fecha])

def Crear_nuevo_Cliente(cedula, tipo, nombre, apellido1, apellido2):
    with connection.cursor() as cursor:
        if apellido1=='':
            apellido1=None;
        if apellido2=='':
            apellido2=None;
        cursor.execute ('INSERT INTO public.cgr_clientes(doc_identidad_o_rif, nombre_cliente, tipo_cliente, primer_apellido, segundo_apellido)VALUES (%s, %s, %s, %s, %s)',
        [cedula, nombre, tipo, apellido1, apellido2])

def Crear_nuevo_viajero(cedula, ciudad, pais, paq_con, nombre1, apellido1, apellido2, sexo, f_nac, nombre2):
     with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_viajeros(id_de_identidad, id_ciudad, id_pais, id_paquete_contrato, primer_nombre, primer_apellido, segundo_apellido, sexo, f_nacimiento, segundo_nombre) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        [cedula, ciudad, pais, paq_con, nombre1, apellido1, apellido2, sexo, f_nac, nombre2])

#--------------------------------------------------------------------------------------------------------

def Ventas_registrar_nuevo_cliente(request):
    if request.method == 'POST':
        form = Form_nuevo_registro_cliente(request.POST)
        cedula = form.data['cedula']
        tipo = form.data['tipo']
        nombre = form.data['nombre']
        apellido1 = form.data['apellido1']
        apellido2 = form.data['apellido2']
        agencia = form.data['agencia']
        f_registro = date.today()
        try:
            Crear_nuevo_Cliente(cedula, tipo, nombre, apellido1, apellido2)
        except:
            messages.error(request, 'Cliente ya agregado en sistema')
            return redirect('Ventas_registrar_nuevo_cliente')
        try:
            Crear_nuevo_Registro_clientes(cedula, agencia, f_registro)
        except:
            messages.error(request, 'Criente ya registrado en agencia de viajes')
            return redirect('Ventas_registrar_nuevo_cliente')
        
        form_i = Form_Instrumentos_de_pago(initial={'doc_identidad_cliente': cedula})
        form_i.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
        return render(request, 'ventas_instrumento_pago.html',{'form':form_i})
    form = Form_nuevo_registro_cliente()
    return render(request, 'ventas_registrar_cliente.html',{'form':form})

def Ventas_intrumento_1(request):
    form = Form_Instrumentos_de_pago(request.POST)
    try:
        form.save()
    except:
        messages.error(request, 'Error al registrar instrumento de pago')
    return redirect ('Show_Clientes')

def Ventas_intrumento_2(request):
    form = Form_Instrumentos_de_pago(request.POST)
    try:
        form.save()
    except:
        messages.error(request, 'Error al registrar instrumento de pago')
    cedula = form.data['doc_identidad_cliente']
    form_i = Form_Instrumentos_de_pago(initial={'doc_identidad_cliente': cedula})
    form_i.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
    return render(request, 'ventas_instrumento_pago.html',{'form':form_i})

def Ventas_crear_nuevo_viajero(request):
    if request.method == 'POST':
        form = Form_nuevo_registro_cliente(request.POST)

        cedula = form.data['cedula']
        nombre1 = form.data['nombre1']
        nombre2 = form.data['nombre2']
        apellido1 = form.data['apellido1']
        apellido2 = form.data['apellido2']
        sexo = form.data['sexo']
        f_nacimento = form.data['f_nacimento']
        ciudad = form.data['ciudad']
        pais_de_ciudad = Ciudades.objects.get(id_ciudad=ciudad)
        pais_de_ciudad = Paises.objects.get(nombre_pais=pais_de_ciudad.id_pais)
        pais_de_ciudad = pais_de_ciudad.id_pais
        pasaporte = form.data['pasaporte']
        pais = form.data['pais']
        paquete = form.data['paquete']
        agencia = Paquetes_contrato.objects.get(numero_factura=paquete)
        agencia = agencia.id_agencia
        f_registro = form.data['f_registro']

        try:
            Crear_nuevo_viajero(cedula, ciudad, pais_de_ciudad, paquete, nombre1, apellido1, apellido2, sexo, f_nacimento, nombre2)
        except:
            messages.error(request, 'Error al agregar Viajero')
            return redirect('ventas_registrar_viajero')
        try:
            Crear_PAI_VIA(cedula, pais, pasaporte)
        except:
            messages.error(request, 'Error al agregar pasaporte viajero')
            return redirect('ventas_registrar_viajero')
        try:
            Crear_Registro_viajeros(agencia, cedula, f_registro, '1')
        except:
            messages.error(request, 'Error al registrar viajero')
            return redirect('ventas_registrar_viajero')

        return redirect('Show_Viajeros')
    
    form = Form_nuevo_registro_viajero()
    return render(request, 'ventas_registrar_viajero.html',{'form':form})