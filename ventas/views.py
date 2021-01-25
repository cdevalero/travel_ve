from django import http
from ventas.forms import *
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import timedelta
from administration.sql_functions import *
from administration.forms import Form_Instrumentos_de_pago
from datetime import date

def index(request):
    return render(request, 'index.html')

def Buscar_Paquete(request):
    if request.method == 'POST':
        form = Form_Buscar_paquerte(request.POST)
        if form.is_valid():

            try:
                agencia = form.data['agencia']
            except:
                agencia = ''
            try:
                personas = form.data['personas']
            except:
                personas = ''
            
            try:
                ciudad = form.data['ciudad']
            except:
                ciudad = ''

            try:
                fecha = form.data['fecha']
            except:
                fecha = ''

            paquete = Paquetes.objects.filter(disponible=True)
            
            if agencia != '':
                paquete = paquete.filter(id_agencia=agencia)
            if personas != '':
                paquete = paquete.filter(numero_personas= personas)

            if ciudad != '':
                no_en = paquete 
                try:
                    itinerarios = Itinerarios.objects.filter(id_ciudad=int(ciudad))
                except Itinerarios.DoesNotExist: 
                    return render(request, 'buscar.html')
                for i in itinerarios:
                    no_en = no_en.exclude(id_paquete=i.id_paquete)
                paquete = paquete.difference(no_en)#

            if fecha != '':
                no_en = paquete 
                try:
                    fechas = Calendarios_anuales.objects.filter(f_salida__range=(form.cleaned_data.get('fecha')-timedelta(days=7),form.cleaned_data.get('fecha')+timedelta(days=7)))
                except Calendarios_anuales.DoesNotExist: 
                    return render(request, 'buscar.html')
                for i in fechas:
                    no_en = no_en.exclude(id_paquete=i.id_paquete)
                paquete = paquete.difference(no_en)

            itinerarios = Itinerarios.objects.all()
            city = Ciudades.objects.all()
            precio = Precios_paquetes.objects.all()
            pais = Paises.objects.all()

            for i in itinerarios:
                for p in pais:
                    if i.id_pais == p.id_pais:
                        for pre in precio:
                            if pre.id_paquete == i.id_paquete:
                                if p.continente_pais == 'Europa':
                                    pre.valor = int(int(pre.valor)/1.22)

            return render(request, 'ver_paquetes.html',{'paquetes':paquete, 'ciudades':city, 'precio':precio, 'itinerarios':itinerarios,'pais': pais})
    form = Form_Buscar_paquerte()
    return render(request, 'buscar.html',{'form':form})

def ver_mas_paquete(request, id):
    paquete = Paquetes.objects.get(id_paquete=id)
    precio = Precios_paquetes.objects.filter(id_paquete=id)
    calendario = Calendarios_anuales.objects.filter(id_paquete=id)
    itinerario = Itinerarios.objects.filter(id_paquete=id)
    atracciones = ITN_ATR.objects.filter(id_paquete= id)
    detalle = Detalles_servicios.objects.filter(id_paquete= id)

    alo_det = ALO_DET.objects.filter(id_paquete= id)

    a_atracciones = Atracciones.objects.all()
    a_ciudades = Ciudades.objects.all() 
    a_alojamiento = Alojamientos.objects.all()
    pais = Paises.objects.all()

    for i in itinerario:
        for p in pais:
            if i.id_pais == p.id_pais:
                for pre in precio:
                    if pre.id_paquete == i.id_paquete:
                            if p.continente_pais == 'Europa':
                                pre.valor = int(int(pre.valor)/1.22)
    
    return render(request, 'ver_mas_paq.html',{     'paq':paquete, 
                                                    'precio': precio, 
                                                    'calendario': calendario, 
                                                    'itinerario':itinerario,
                                                    'atracciones':atracciones,
                                                    'detalle':detalle,
                                                    'alo_det': alo_det,
                                                    'nombre_atr': a_atracciones,
                                                    'nombre_c':a_ciudades,
                                                    'pais':pais,
                                                    'nombre_alo': a_alojamiento
    })

# Proceso de Venta ---------------------------------------

def seleccionar_asesor(request):
    if request.method == 'POST':
        form = Form_Buscar_paquerte(request.POST)
        try:
            agente = form.data['agente']
        except:
            agente = '0'
        cliente = form.data['cliente']

        tipo = form.data['tipo']
        nombre = form.data['nombre']
        try:
            apellido1 = form.data['apellido1']
        except:
            apellido1 = ''
        try:
            apellido2 = form.data['apellido2']
        except:
            apellido2 = ''
        try:
            validacion = Clientes.objects.get(doc_identidad_o_rif= cliente)
        except Clientes.DoesNotExist:
            Crear_nuevo_Cliente(cliente, tipo, nombre, apellido1, apellido2)

        return redirect('ventas_buscar_paquete', agente, cliente)
        
    form = Form_Seleccionar_agente()
    return render(request, 'venta/seleccionar_cli_age.html',{'form':form})

def ventas_buscar_paquete(request, agente, cliente):
    if request.method == 'POST':
        form = Form_Buscar_paquerte(request.POST)
        if form.is_valid():
            try:
                agencia = form.data['agencia']
            except:
                agencia = ''
            try:
                personas = form.data['personas']
            except:
                personas = ''
            try:
                ciudad = form.data['ciudad']
            except:
                ciudad = ''
            try:
                fecha = form.data['fecha']
            except:
                fecha = ''
            cliente = form.data['cliente']
            agente = form.data['agente']

            paquete = Paquetes.objects.filter(disponible=True)
            
            if agencia != '':
                paquete = paquete.filter(id_agencia=agencia)
            if personas != '':
                paquete = paquete.filter(numero_personas= personas)

            if ciudad != '':
                no_en = paquete 
                try:
                    itinerarios = Itinerarios.objects.filter(id_ciudad=int(ciudad))
                except Itinerarios.DoesNotExist: 
                    return redirect('ventas_buscar_paquete', agente, cliente)
                for i in itinerarios:
                    no_en = no_en.exclude(id_paquete=i.id_paquete)
                paquete = paquete.difference(no_en)#

            if fecha != '':
                no_en = paquete 
                try:
                    fechas = Calendarios_anuales.objects.filter(f_salida__range=(form.cleaned_data.get('fecha')-timedelta(days=7),form.cleaned_data.get('fecha')+timedelta(days=7)))
                except Calendarios_anuales.DoesNotExist: 
                    return redirect('ventas_buscar_paquete', agente, cliente)
                for i in fechas:
                    no_en = no_en.exclude(id_paquete=i.id_paquete)
                paquete = paquete.difference(no_en)

            itinerarios = Itinerarios.objects.all()
            city = Ciudades.objects.all()
            precio = Precios_paquetes.objects.all()
            pais = Paises.objects.all()

            for i in itinerarios:
                for p in pais:
                    if i.id_pais == p.id_pais:
                        for pre in precio:
                            if pre.id_paquete == i.id_paquete:
                                if p.continente_pais == 'Europa':
                                    pre.valor = int(int(pre.valor)/1.22)
            return render(request, 'venta/ventas_ver_paquetes.html',{'paquetes':paquete, 'ciudades':city, 'precio':precio, 'itinerarios':itinerarios,'pais': pais, 'cliente':cliente, 'agente':agente})
            
    form = Form_ventas_buscar_paquete(initial={'agente': agente, 'cliente': cliente})
    form.fields['cliente'].widget.attrs['hidden'] = True
    form.fields['agente'].widget.attrs['hidden'] = True
    return render(request, 'venta/ventas_buscar_paquete.html',{'form':form})

def ventas_ver_mas_paquete(request, id, agente, cliente):
    paquete = Paquetes.objects.get(id_paquete=id)
    precio = Precios_paquetes.objects.filter(id_paquete=id)
    calendario = Calendarios_anuales.objects.filter(id_paquete=id)
    itinerario = Itinerarios.objects.filter(id_paquete=id)
    atracciones = ITN_ATR.objects.filter(id_paquete= id)
    detalle = Detalles_servicios.objects.filter(id_paquete= id)

    alo_det = ALO_DET.objects.filter(id_paquete= id)

    a_atracciones = Atracciones.objects.all()
    a_ciudades = Ciudades.objects.all() 
    a_alojamiento = Alojamientos.objects.all()
    pais = Paises.objects.all()

    for i in itinerario:
        for p in pais:
            if i.id_pais == p.id_pais:
                for pre in precio:
                    if pre.id_paquete == i.id_paquete:
                            if p.continente_pais == 'Europa':
                                pre.valor = int(int(pre.valor)/1.22)
    
    return render(request, 'venta/ventas_ver_mas.html',{     'paq':paquete, 
                                                    'precio': precio, 
                                                    'calendario': calendario, 
                                                    'itinerario':itinerario,
                                                    'atracciones':atracciones,
                                                    'detalle':detalle,
                                                    'alo_det': alo_det,
                                                    'nombre_atr': a_atracciones,
                                                    'nombre_c':a_ciudades,
                                                    'pais':pais,
                                                    'nombre_alo': a_alojamiento,
                                                    'age': agente,
                                                    'cli': cliente
    })

def ventas_comprar_paquete(request, paquete, agente, cliente, precio, fecha, agencia):
    agencia = Agencias_de_viajes.objects.get(nombre= agencia)
    agencia = agencia.id_agencia
    
    form = Form_ventas_descuneto_forma(agencia, fecha)
    return render(request, 'venta/ventas_des_for.html',{  'paquete':paquete, 
                                                    'agente': agente, 
                                                    'cliente': cliente, 
                                                    'precio':precio,
                                                    'fecha':fecha,
                                                    'agencia': agencia,
                                                    'form': form
    })

def ventas_presupuesto(request, paquete, agente, cliente, precio, fecha, agencia):
    form = Form_Buscar_paquerte(request.POST)
    tipo = form.data['tipo']
    try:
        descuento = form.data['descuento']
    except:
        descuento = ''
    email = form.data['email']

    viajero = Paquetes.objects.get(id_paquete= paquete)

    ventas_registrar_cliente(cliente, agencia)
    Crear_paquete_presupuesto(paquete, agencia, cliente, precio, date.today(), email, precio, viajero, fecha, agente)
    contrato = Paquetes_contrato.objects.latest('numero_factura')

    form_i = Form_ventas_instrumento(initial={'max': precio})
    form_i.fields['max'].widget.attrs['readonly'] = True
    return render(request, 'venta/ventas_instrumento.html',
    {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})

def ventas_registrar_cliente(cliente, agencia):
    try:
        validacion = Registro_clientes.objects.get(id_cliente= cliente, id_agencia=agencia)
    except Registro_clientes.DoesNotExist:
        Crear_Registro_clientes(cliente, agencia, date.today(), 1)

def ventas_intrumento(request, cliente, contrato, tipo, descuento):

    form = Form_Instrumentos_de_pago(request.POST)
    tipo_f = tipo
    max = int(form.data['max'])
    monto = int(form.data['monto'])
    tipo_i = form.data['tipo']

    try:
        banco = form.data['banco']
    except:
        banco= ''
    try:
        numero = form.data['numero']
    except:
        numero= ''
    try:
        email = form.data['email']
    except:
        email= ''

    if tipo_i == 'zelle' and banco!='':
        messages.error(request, 'El tipo de instrumento no debe estar vinculado con un banco')
        form_i = Form_ventas_instrumento(initial={'max': form.data['max']})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})

    if tipo_i== 'zelle' and numero=='':
        messages.error(request, 'Falto Vincular numero zelle')
        form_i = Form_ventas_instrumento(initial={'max': form.data['max']})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})

    if tipo_i== 'zelle' and email=='':
        messages.error(request, 'Falto Vincular Email zelle')
        form_i = Form_ventas_instrumento(initial={'max': form.data['max']})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})

    if tipo_i!= 'zelle' and banco=='':
        messages.error(request, 'El tipo de instrumento debe estar vinculado con un banco')
        form_i = Form_ventas_instrumento(initial={'max': form.data['max']})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})

    if tipo_i!= 'zelle' and numero!='':
        messages.error(request, 'No se puede vincular numero zelle')
        form_i = Form_ventas_instrumento(initial={'max': form.data['max']})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})

    if tipo_i!= 'zelle' and email!='':
        messages.error(request, 'No se puede vincular email zelle')
        form_i = Form_ventas_instrumento(initial={'max': form.data['max']})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})

    if max < monto:
        messages.error(request, 'Monto inadecuado')
        form_i = Form_ventas_instrumento(initial={'max': form.data['max']})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})

    if Crear_nuevo_instrumento(cliente, monto, tipo_i, banco, numero, email)== 1:
        messages.error(request, 'Error al crear Intrumento')
        form_i = Form_ventas_instrumento(initial={'max': form.data['max']})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})
    
    instrumento = Instrumentos_de_pago.objects.latest('id_instrumento')

    try:
        Crear_Forma_de_pago(instrumento, cliente, contrato, tipo_f)
    except:
        max = max + monto
    
    max = max - monto

    if max!=0:
        form_i = Form_ventas_instrumento(initial={'max': max})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})
    
    else:
        return HttpResponse('hola')

