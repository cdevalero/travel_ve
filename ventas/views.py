from django import http
from ventas.forms import *
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import timedelta
from administration.sql_functions import *
from administration.forms import Form_Instrumentos_de_pago, Form_nuevo_registro_viajero_compra
from datetime import date, datetime

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

            try:
                area = form.data['area']
            except:
                area = ''

            paquete = Paquetes.objects.filter(disponible=True)
            
            if agencia != '':
                paquete = paquete.filter(id_agencia=agencia)
            if personas != '':
                paquete = paquete.filter(numero_personas= personas)

            no_en = paquete

            if ciudad != '':
                #no_en = paquete
                try:
                    itinerarios = Itinerarios.objects.filter(id_ciudad=int(ciudad))
                except Itinerarios.DoesNotExist: 
                    return render(request, 'buscar.html')
                for i in itinerarios:
                    no_en = no_en.exclude(id_paquete=i.id_paquete)
                #paquete = paquete.difference(no_en)

            if fecha != '':
                #no_en = paquete 
                try:
                    fechas = Calendarios_anuales.objects.filter(f_salida__range=(form.cleaned_data.get('fecha')-timedelta(days=7),form.cleaned_data.get('fecha')+timedelta(days=7)))
                except Calendarios_anuales.DoesNotExist: 
                    return render(request, 'buscar.html')
                for i in fechas:
                    no_en = no_en.exclude(id_paquete=i.id_paquete)
                #paquete = paquete.difference(no_en)

            if area != '':
                try:
                    especialidad = Especializaciones.objects.filter(id_areas_de_interes= area)
                except Especializaciones.DoesNotExist:
                    return render(request, 'buscar.html')
                for i in especialidad:
                    no_en = no_en.exclude(id_paquete= i.id_paquete)

            if fecha != '' or ciudad != '' or area != '':
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
        if agente == '':
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

            try:
                area = form.data['area']
            except:
                area = ''

            cliente = form.data['cliente']
            agente = form.data['agente']

            paquete = Paquetes.objects.filter(disponible=True)
            
            if agencia != '':
                paquete = paquete.filter(id_agencia=agencia)
            if personas != '':
                paquete = paquete.filter(numero_personas= personas)

            if ciudad != '':
                #no_en = paquete
                try:
                    itinerarios = Itinerarios.objects.filter(id_ciudad=int(ciudad))
                except Itinerarios.DoesNotExist: 
                    return redirect('ventas_buscar_paquete', agente, cliente)
                for i in itinerarios:
                    no_en = no_en.exclude(id_paquete=i.id_paquete)
                #paquete = paquete.difference(no_en)

            if fecha != '':
                #no_en = paquete 
                try:
                    fechas = Calendarios_anuales.objects.filter(f_salida__range=(form.cleaned_data.get('fecha')-timedelta(days=7),form.cleaned_data.get('fecha')+timedelta(days=7)))
                except Calendarios_anuales.DoesNotExist: 
                    return redirect('ventas_buscar_paquete', agente, cliente)
                for i in fechas:
                    no_en = no_en.exclude(id_paquete=i.id_paquete)
                #paquete = paquete.difference(no_en)

            if area != '':
                try:
                    especialidad = Especializaciones.objects.filter(id_areas_de_interes= area)
                except Especializaciones.DoesNotExist:
                    return render(request, 'buscar.html')
                for i in especialidad:
                    no_en = no_en.exclude(id_paquete= i.id_paquete)

            if fecha != '' or ciudad != '' or area != '':
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
        descuento = '0'
    if descuento == '':
        descuento = '0'
    email = form.data['email']

    euro = 0
    itinerario = Itinerarios.objects.filter(id_paquete=paquete)
    a_ciudades = Ciudades.objects.all() 
    pais = Paises.objects.all()

    for i in itinerario:
        for c in a_ciudades:
            if i.id_ciudad == c.id_ciudad:
                for p in pais:
                    if str(c.id_pais) == p.nombre_pais:
                        if p.continente_pais == 'Europa':
                            euro = euro + 1
    if euro >0:
        precio = int(int(precio)*1.22)

    viajero = Paquetes.objects.get(id_paquete= paquete)

    ventas_registrar_cliente(cliente, agencia)
    if Crear_paquete_presupuesto(paquete, agencia, cliente, precio, date.today(), email, precio, viajero.numero_personas, fecha, agente)==1:
        return HttpResponse('error')

    contrato = Paquetes_contrato.objects.latest('numero_factura')

    form_i = Form_ventas_instrumento(initial={'max': int(precio)})
    form_i.fields['max'].widget.attrs['readonly'] = True
    
    return render(request, 'venta/ventas_instrumento.html',
    {'cliente':cliente, 'contrato':contrato.numero_factura, 'tipo': tipo, 'descuento':descuento, 'form':form_i})

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
        messages.error(request, 'Error al registrar Instrumento')
        form_i = Form_ventas_instrumento(initial={'max': form.data['max']})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})
    
    instrumento = Instrumentos_de_pago.objects.latest('id_instrumento')

    try:
        Crear_Forma_de_pago(instrumento.id_instrumento, cliente, contrato, tipo_f)
    except:
        messages.error(request, instrumento.id_instrumento)
        max = max + monto
    
    max = max - monto

    if max!=0:
        form_i = Form_ventas_instrumento(initial={'max': max})
        form_i.fields['max'].widget.attrs['readonly'] = True
        return render(request, 'venta/ventas_instrumento.html',
        {'cliente':cliente, 'contrato':contrato, 'tipo': tipo, 'descuento':descuento, 'form':form_i})
    
    else:
        return ventas_ver_presupuesto(request, contrato, tipo, descuento)

def ventas_ver_presupuesto(request, id_contrato, tipo, descuento):
    paq_contrato = Paquetes_contrato.objects.get(numero_factura= id_contrato)

    paquete = Paquetes.objects.get(id_paquete=paq_contrato.id_paquete)

    precio = paq_contrato.presupuesto

    email = paq_contrato.email_validacion

    cliente = Clientes.objects.get(doc_identidad_o_rif= paq_contrato.id_reg_cliente)

    formas_pago = Formas_de_pago.objects.filter(id_paquete_contrato= id_contrato)

    fecha = paq_contrato.f_viaje

    itinerario = Itinerarios.objects.filter(id_paquete=paq_contrato.id_paquete)

    atracciones = ITN_ATR.objects.filter(id_paquete= paq_contrato.id_paquete)

    detalle = Detalles_servicios.objects.filter(id_paquete= paq_contrato.id_paquete)

    alo_det = ALO_DET.objects.filter(id_paquete= paq_contrato.id_paquete)

    if descuento != '0':
        descuento = Descuentos.objects.get(id_descuento= descuento)
    else:
        descuento = None

    euro = 0
    instrumento = Instrumentos_de_pago.objects.filter(doc_identidad_cliente=paq_contrato.id_reg_cliente)
    a_atracciones = Atracciones.objects.all()
    a_ciudades = Ciudades.objects.all() 
    a_alojamiento = Alojamientos.objects.all()
    pais = Paises.objects.all()
 
    return render(request, 'venta/presupuesto.html',{     'paq':paquete, #
                                                    'valor': precio, #
                                                    'email': email,
                                                    'cliente': cliente,#
                                                    'formas': formas_pago, #
                                                    'fecha': fecha,#
                                                    'itinerario':itinerario,#
                                                    'atracciones':atracciones,#
                                                    'detalle':detalle,#
                                                    'alo_det': alo_det,#
                                                    'nombre_atr': a_atracciones,#
                                                    'nombre_c':a_ciudades,#
                                                    'euro':euro,#
                                                    'instrumento':instrumento,#
                                                    'tipo':tipo,#
                                                    'descuento':descuento,#
                                                    'contrato':id_contrato,#
                                                    'nombre_alo': a_alojamiento,
                                                    'numero': paq_contrato.numer_de_viajeros
    })

#---------------------------------------

def confirmar_presupuesto(request, contrato, numero, tipo, descuento):
    form = Form_nuevo_registro_viajero_compra(initial={'f_registro': date.today(), 'paquete':contrato})
    form.fields['f_registro'].widget.attrs['hidden'] = True
    form.fields['paquete'].widget.attrs['hidden'] = True
    return render(request, 'venta/ventas_add_viajero.html',{'form':form, 'cuenta':1, 'numero':numero, 'tipo':tipo, 'descuento':descuento, 'contrato':contrato})

def ventas_registrar_viajeros(request, contrato, cuenta, numero, tipo, descuento):
    if int(cuenta) >= int(numero):
        return redirect('ventas_registrar_viajeros_terminar', contrato, cuenta, numero, tipo, descuento)

    form = Form_nuevo_registro_viajero_compra(request.POST)

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

    '''if descuento != '0':
        Calcular_Descuento(contrato, descuento, f_nacimento)'''

    try:
        validacion = Viajeros.objects.get(id_de_identidad= cedula)
    except Viajeros.DoesNotExist:
        if Crear_nuevo_viajero(cedula, ciudad, pais_de_ciudad, paquete, nombre1, apellido1, apellido2, sexo, f_nacimento, nombre2) == 1:
            messages.error(request, 'Error al agregar Viajero')
            return render(request, 'venta/ventas_add_viajero.html',{'form':form, 'cuenta':cuenta, 'numero':numero, 'tipo':tipo, 'descuento':descuento, 'contrato':contrato})

    try:
        validacion = PAI_VIA.objects.get(id_viajero=cedula, id_pais=pais)
    except PAI_VIA.DoesNotExist:
        if Crear_nuevo_PAI_VIA(cedula, pais, pasaporte) == 1:
            messages.error(request, 'Error al agregar pasaporte viajero')
            return render(request, 'venta/ventas_add_viajero.html',{'form':form, 'cuenta':cuenta, 'numero':numero, 'tipo':tipo, 'descuento':descuento, 'contrato':contrato})

    try:
        validacion = Registro_viajeros.objects.get(id_viajero=cedula, id_agencia=agencia)
    except Registro_viajeros.DoesNotExist:
        if Crear_Registro_viajeros(agencia, cedula, f_registro, '1') ==1:
            messages.error(request, 'Error al registrar viajero')
            return render(request, 'venta/ventas_add_viajero.html',{'form':form, 'cuenta':cuenta, 'numero':numero, 'tipo':tipo, 'descuento':descuento, 'contrato':contrato})

    cuenta = int(cuenta) + 1

    form = Form_nuevo_registro_viajero_compra(initial={'f_registro': date.today(), 'paquete':contrato})
    form.fields['f_registro'].widget.attrs['hidden'] = True
    form.fields['paquete'].widget.attrs['hidden'] = True
    return render(request, 'venta/ventas_add_viajero.html',{'form':form, 'cuenta':cuenta, 'numero':numero, 'tipo':tipo, 'descuento':descuento, 'contrato':contrato})

def ventas_registrar_viajeros_terminar(request, contrato, cuenta, numero, tipo, descuento):

    form = Form_nuevo_registro_viajero_compra(request.POST)

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

    '''if descuento != '0':
        Calcular_Descuento(contrato, descuento, f_nacimento)'''

    try:
        validacion = Viajeros.objects.get(id_de_identidad= cedula)
    except Viajeros.DoesNotExist:
        if Crear_nuevo_viajero(cedula, ciudad, pais_de_ciudad, paquete, nombre1, apellido1, apellido2, sexo, f_nacimento, nombre2) == 1:
            messages.error(request, 'Error al agregar Viajero')
            return render(request, 'venta/ventas_add_viajero.html',{'form':form, 'cuenta':cuenta, 'numero':numero, 'tipo':tipo, 'descuento':descuento, 'contrato':contrato})

    try:
        validacion = PAI_VIA.objects.get(id_viajero=cedula, id_pais=pais)
    except PAI_VIA.DoesNotExist:
        if Crear_nuevo_PAI_VIA(cedula, pais, pasaporte) == 1:
            messages.error(request, 'Error al agregar pasaporte viajero')
            return render(request, 'venta/ventas_add_viajero.html',{'form':form, 'cuenta':cuenta, 'numero':numero, 'tipo':tipo, 'descuento':descuento, 'contrato':contrato})

    try:
        validacion = Registro_viajeros.objects.get(id_viajero=cedula, id_agencia=agencia)
    except Registro_viajeros.DoesNotExist:
        if Crear_Registro_viajeros(agencia, cedula, f_registro, '1') ==1:
            messages.error(request, 'Error al registrar viajero')
            return render(request, 'venta/ventas_add_viajero.html',{'form':form, 'cuenta':cuenta, 'numero':numero, 'tipo':tipo, 'descuento':descuento, 'contrato':contrato})

    return redirect('ver_contrato', contrato, cuenta, tipo, descuento)

def ver_contrato(request, id_contrato, numero, tipo, descuento):

    Cambiar_paquete_contrato(date.today(), numero, id_contrato)

    viajero = Viajeros.objects.filter(id_paquete_contrato= id_contrato)

    pasaporte = PAI_VIA.objects.all()

    paq_contrato = Paquetes_contrato.objects.get(numero_factura= id_contrato)

    paquete = Paquetes.objects.get(id_paquete=paq_contrato.id_paquete)

    precio = paq_contrato.presupuesto

    email = paq_contrato.email_validacion

    cliente = Clientes.objects.get(doc_identidad_o_rif= paq_contrato.id_reg_cliente)

    formas_pago = Formas_de_pago.objects.filter(id_paquete_contrato= id_contrato)

    fecha = paq_contrato.f_viaje

    itinerario = Itinerarios.objects.filter(id_paquete=paq_contrato.id_paquete)

    atracciones = ITN_ATR.objects.filter(id_paquete= paq_contrato.id_paquete)

    detalle = Detalles_servicios.objects.filter(id_paquete= paq_contrato.id_paquete)

    alo_det = ALO_DET.objects.filter(id_paquete= paq_contrato.id_paquete)

    registro_cli = Registro_clientes.objects.all()

    euro = 0
    instrumento = Instrumentos_de_pago.objects.filter(doc_identidad_cliente=paq_contrato.id_reg_cliente)
    a_atracciones = Atracciones.objects.all()
    a_ciudades = Ciudades.objects.all() 
    a_alojamiento = Alojamientos.objects.all()
    pais = Paises.objects.all()

    if descuento == '0':
        descuento = None

    prueba_fecha = fecha
    prueba_dias = Itinerarios.objects.filter(id_paquete=paq_contrato.id_paquete)

    for p in prueba_dias:
        dia = int(p.tiempo_estadia)
        if p.orden == 1:
            p.tiempo_estadia = prueba_fecha
        else:
            p.tiempo_estadia = prueba_fecha + timedelta(days=dia)
        prueba_fecha= prueba_fecha 

    return render(request, 'venta/contrato.html',{     'paq':paquete, #
                                                    'valor': precio, #
                                                    'email': email,
                                                    'cliente': cliente,#
                                                    'formas': formas_pago, #
                                                    'fecha': fecha,#
                                                    'itinerario':itinerario,#
                                                    'atracciones':atracciones,#
                                                    'detalle':detalle,#
                                                    'alo_det': alo_det,#
                                                    'nombre_atr': a_atracciones,#
                                                    'nombre_c':a_ciudades,#
                                                    'euro':euro,#
                                                    'instrumento':instrumento,#
                                                    'tipo':tipo,#
                                                    'descuento':descuento,#
                                                    'pasaporte': pasaporte,
                                                    'contrato':id_contrato,#
                                                    'nombre_alo': a_alojamiento,
                                                    'viajero': viajero,
                                                    'registro_cli': registro_cli,
                                                    'numero': paq_contrato.numer_de_viajeros,
                                                    'prueba_dias': prueba_dias
    })



def calcular_edad_agnios(fecha_nacimiento):
    fecha_nacimiento = datetime.strptime(fecha_nacimiento,'%Y-%m-%d')
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nacimiento.year
    resultado -= ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return resultado

def Calcular_Descuento(contrato, descuento, fecha):
    contrato = Paquetes_contrato.objects.get(numero_factura= contrato)
    descuento = Descuentos.objects.get(id_descuento= descuento)

    if descuento.tipo_descuento == 'descnino':
        validar = calcular_edad_agnios(fecha)
        if validar >= 18:
            porcentaje = int(descuento.porcentaje)/100
            valor = contrato.total_costo_calculado

