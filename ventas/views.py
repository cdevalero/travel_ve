from django.db import connection
from administration.models import Agencias_de_viajes
from django.http.response import HttpResponse
from ventas.forms import Form_nuevo_registro_cliente
from django.shortcuts import redirect, render
from datetime import date
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def Crear_nuevo_Registro_clientes(cliente, agencia, fecha, numero):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_registro_clientes(id_cliente, id_agencia, f_registro, numero_registro) VALUES (%s, %s, %s, %s)', 
        [cliente, agencia, fecha, numero])

def Crear_nuevo_Cliente(cedula, tipo, nombre, apellido1, apellido2):
    with connection.cursor() as cursor:
        cursor.execute ('INSERT INTO public.cgr_clientes(doc_identidad_o_rif, nombre_cliente, tipo_cliente, primer_apellido, segundo_apellido)VALUES (%s, %s, %s, %s, %s)',
        [cedula, nombre, tipo, apellido1, apellido2])


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
        numero = form.data['numero']
        try:
            Crear_nuevo_Cliente(cedula, tipo, nombre, apellido1, apellido2)
        except:
            messages.error(request, 'Entrada Invalida1')
            return redirect('Ventas_registrar_nuevo_cliente')
        try:
            Crear_nuevo_Registro_clientes(cedula, agencia, f_registro, numero)
        except:
            messages.error(request, 'Entrada Invalida2')
            return redirect('Ventas_registrar_nuevo_cliente')
        return redirect('index')
    form = Form_nuevo_registro_cliente()
    return render(request, 'ventas_registrar_cliente.html',{'form':form})

