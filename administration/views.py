from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from datetime import timedelta

# SHOW

def Show_bancos(request):
    obj = Bancos.objects.all()
    return render(request, 'show/ShowBancos.html', {'obj': obj})

def Show_Clientes(request):
    obj = Clientes.objects.all()
    return render(request, 'show/ShowClientes.html', {'obj': obj})

def Show_Areas_de_interes(request):
    obj = Areas_de_interes.objects.all()
    return render(request, 'show/ShowArea_de_Interes.html', {'obj': obj})

def Show_paises(request):
    obj = Paises.objects.all()
    return render(request, 'show/ShowPaises.html', {'obj': obj})

def Show_rallies(request):
    obj = Rallies.objects.all()
    return render(request, 'show/ShowRallie.html', {'obj': obj})

def Show_premios(request):
    obj = Premios.objects.all()
    return render(request, 'show/ShowPremios.html', {'obj': obj})

def Show_Ciudades(request):
    obj = Ciudades.objects.all()
    return render(request, 'show/ShowCiudades.html', {'obj': obj})

def Show_Atracciones(request):
    obj = Atracciones.objects.all()
    return render(request, 'show/ShowAtracciones.html', {'obj': obj})

def Show_Circuitos(request):
    obj = Circuitos.objects.all()
    return render(request, 'show/ShowCircuitos.html', {'obj': obj})

def Show_atr_cir(request):
    obj = ATR_CIR.objects.all()
    return render(request, 'show/ShowATR_CIR.html', {'obj': obj})

def Show_Agencias_de_viajes(request):
    obj = Agencias_de_viajes.objects.all()
    return render(request, 'show/ShowAgencias_de_viajes.html', {'obj': obj})

def Show_AGE_AGE(request):
    obj = AGE_AGE.objects.all()
    return render(request, 'show/ShowAGE_AGE.html', {'obj': obj})

def Show_cupos(request):
    obj = Cupos.objects.all()
    return render(request, 'show/ShowCupos.html', {'obj': obj})

def Show_Registro_clientes(request):
    obj = Registro_clientes.objects.all()
    return render(request, 'show/ShowRegistro_clientes.html', {'obj': obj})

def Show_Alojamientos(request):
    obj = Alojamientos.objects.all()
    return render(request, 'show/ShowAlojamientos.html', {'obj': obj})

def Show_Proveedores(request):
    obj = Proveedores.objects.all()
    return render(request, 'show/ShowProveedores.html', {'obj': obj})

def Show_pro_age(request):
    obj = PRO_AGE.objects.all()
    return render(request, 'show/ShowPRO_AGE.html', {'obj': obj})

def Show_Asesores_de_viajes(request):
    obj = Asesores_de_viajes.objects.all()
    return render(request, 'show/ShowAsesores_de_viajes.html', {'obj': obj})

def Show_Paquetes(request):
    obj = Paquetes.objects.all()
    return render(request, 'show/ShowPaquetes.html', {'obj': obj})

def Show_Especializaciones(request):
    obj = Especializaciones.objects.all()
    return render(request, 'show/ShowEspecializaciones.html', {'obj': obj})

def Show_Precios_paquetes(request):
    obj = Precios_paquetes.objects.all()
    return render(request, 'show/ShowPrecios_paquetes.html', {'obj': obj})

def Show_Calendarios_anuales(request):
    obj = Calendarios_anuales.objects.all()
    return render(request, 'show/ShowCalendarios_anuales.html', {'obj': obj})

def Show_Descuentos(request):
    obj = Descuentos.objects.all()
    return render(request, 'show/ShowDescuentos.html', {'obj': obj})

def Show_Intinerarios(request):
    obj = Itinerarios.objects.all()
    return render(request, 'show/ShowIntinerarios.html', {'obj': obj})

def Show_ITN_ATR(request):
    obj = ITN_ATR.objects.all()
    return render(request, 'show/ShowITN_ATR.html', {'obj': obj})

def Show_Detalles_servicios(request):
    obj = Detalles_servicios.objects.all()
    return render(request, 'show/ShowDetalles_servicios.html', {'obj': obj})

def Show_ALO_DET(request):
    obj = ALO_DET.objects.all()
    return render(request, 'show/ShowALO_DET.html', {'obj': obj})

def Show_Instrumentos_de_pago(request):
    obj = Instrumentos_de_pago.objects.all()
    return render(request, 'show/ShowInstrumentos_de_pago.html', {'obj': obj})

def Show_Paquetes_contrato(request):
    obj = Paquetes_contrato.objects.all()
    return render(request, 'show/ShowPaquetes_contrato.html', {'obj': obj})

def Show_Formas_de_pago(request):
    obj = Formas_de_pago.objects.all()
    return render(request, 'show/ShowFormas_de_pago.html', {'obj': obj})

def Show_Viajeros(request):
    obj = Viajeros.objects.all()
    return render(request, 'show/ShowViajeros.html', {'obj': obj})

def Show_PAI_VIA(request):
    obj = PAI_VIA.objects.all()
    return render(request, 'show/ShowPAI_VIA.html', {'obj': obj})

def Show_Registro_viajeros(request):
    obj = Registro_viajeros.objects.all()
    return render(request, 'show/ShowRegistros_viajeros.html', {'obj': obj})

def Show_Detalle_viajeros(request):
    obj = Detalle_viajeros.objects.all()
    return render(request, 'show/ShowDetalle_viajeros.html', {'obj': obj})

def Show_Participantes(request):
    obj = Participantes.objects.all()
    return render(request, 'show/ShowParticipantes.html', {'obj': obj})

def Show_Puntuaciones(request):
    obj = Puntuaciones.objects.all()
    return render(request, 'show/ShowPuntuaciones.html', {'obj': obj})

#ADD

def Add_Bancos(request):
    if request.method == 'POST':
        form = Form_Bancos(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_bancos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_bancos')
    form = Form_Bancos()
    return render(request, 'create_edit/AddBancos.html',{'form':form})

def Add_Clientes(request):
    if request.method == 'POST':
        form = Form_Clientes(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_Clientes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Clientes')
    form = Form_Clientes()
    return render(request, 'create_edit/AddClientes.html',{'form':form})

def Add_Areas_de_interes(request):
    if request.method == 'POST':
        form = Form_Areas_de_interes(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_Areas_de_interes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Areas_de_interes')
    form = Form_Areas_de_interes()
    return render(request, 'create_edit/AddAreas_de_interes.html',{'form':form})

def Add_Paises(request):
    if request.method == 'POST':
        form = Form_Paises(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_paises')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_paises')
    form = Form_Paises()
    return render(request, 'create_edit/AddPaises.html',{'form':form})

def Add_Rallies(request):
    if request.method == 'POST':
        form = Form_Rallies(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_rallies')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_rallies')
    form = Form_Rallies()
    return render(request, 'create_edit/AddRallies.html',{'form':form})

def Add_Premios(request):
    if request.method == 'POST':
        form = Form_Premios(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_premios')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_premios')
    form = Form_Premios()
    return render(request, 'create_edit/AddPremios.html',{'form':form})

def Add_Ciudades(request):
    if request.method == 'POST':
        form = Form_Ciudades(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_Ciudades')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Ciudades')
    form = Form_Ciudades()
    return render(request, 'create_edit/AddCiudades.html',{'form':form})

def Add_Atracciones(request):
    if request.method == 'POST':
        form = Form_Atracciones(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_Atracciones')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Atracciones')
    form = Form_Atracciones()
    return render(request, 'create_edit/AddAtracciones.html',{'form':form})

def Add_Circuitos(request):
    pass

def Add_ATR_CIR(request):
    pass

def Add_Agencia_de_viajes(request):
    pass

def Add_AGE_AGE(request):
    pass

def Add_Cupos(request):
    pass

def Add_Registro_clientes(request):
    pass

def Add_Alojamientos(request):
    pass

def Add_Proveedores(request):
    pass

def Add_PRO_AGE(request):
    pass

def Add_Asesores_de_viajes(request):
    pass

def Add_Paquetes(request):
    pass

def Add_Especializaciones(request):
    pass

def Add_Precios_paquetes(request):
    pass

def Add_Calendarios_anuales(request):
    pass

def Add_Descuentos(request):
    pass

def Add_Intinerarios(request):
    pass

def Add_ITN_ATR(request):
    pass

def Add_Detalles_servicios(request):
    pass

def Add_ALO_DET(request):
    pass

def Add_Instrumentos_de_pago(request):
    pass

def Add_Paquetes_contrato(request):
    pass

def Add_Formas_de_pago(request):
    pass

def Add_Viajeros(request):
    pass

def Add_PAI_VIA(request):
    pass

def Add_Registro_viajeros(request):
    pass

def Add_Detalle_viajeros(request):
    pass

def Add_Participantes(request):
    pass

def Add_Puntuaciones(request):
    pass

#Delete

def Delete_Bancos(request, id):
    try:
        obj = Bancos.objects.get(pk=id)
    except Bancos.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_bancos')
    obj.delete()
    return redirect('Show_bancos')

def Delete_Clientes(request, id):
    try:
        obj = Clientes.objects.get(pk=id)
    except Clientes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Clientes')
    obj.delete()
    return redirect('Show_Clientes')

def Delete_Areas_de_interes(request, id):
    try:
        obj = Areas_de_interes.objects.get(pk=id)
    except Areas_de_interes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Areas_de_interes')
    obj.delete()
    return redirect('Show_Areas_de_interes')

def Delete_Paises(request, id):
    try:
        obj = Paises.objects.get(pk=id)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_paises')
    obj.delete()
    return redirect('Show_paises')

def Delete_Rallies(request, id):
    try:
        obj = Rallies.objects.get(pk=id)
    except Rallies.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_rallies')
    obj.delete()
    return redirect('Show_rallies')

def Delete_Premios(request, id, id2):
    try:
        rallie = Rallies.objects.get(nombre_rally=id2)
    except Rallies.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_rallies')
    try:
        obj = Premios.objects.filter(id_pais=rallie.id_rally).get(id_premio=id)
    except Premios.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_rallies')
    obj.delete()
    return redirect('Show_rallies')

def Delete_Ciudades(request, id, id2):
    try:
        pais = Paises.objects.get(nombre_pais=id2)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Ciudades')
    try:
        obj = Ciudades.objects.filter(id_pais=pais.id_pais).get(id_ciudad=id)
    except Ciudades.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Ciudades')
    obj.delete()
    return redirect('Show_Ciudades')

def Delete_Atracciones(request, id):
    pass

def Delete_Circuitos(request, id):
    pass

def Delete_ATR_CIR(request, id):
    pass

def Delete_Agencia_de_viajes(request, id):
    pass

def Delete_AGE_AGE(request, id):
    pass

def Delete_Cupos(request, id):
    pass

def Delete_Registro_clientes(request, id):
    pass

def Delete_Alojamientos(request, id):
    pass

def Delete_Proveedores(request, id):
    pass

def Delete_PRO_AGE(request, id):
    pass

def Delete_Asesores_de_viajes(request, id):
    pass

def Delete_Paquetes(request, id):
    pass

def Delete_Especializaciones(request, id):
    pass

def Delete_Precios_paquetes(request, id):
    pass

def Delete_Calendarios_anuales(request, id):
    pass

def Delete_Descuentos(request, id):
    pass

def Delete_Intinerarios(request, id):
    pass

def Delete_ITN_ATR(request, id):
    pass

def Delete_Detalles_servicios(request, id):
    pass

def Delete_ALO_DET(request, id):
    pass

def Delete_Instrumentos_de_pago(request, id):
    pass

def Delete_Paquetes_contrato(request, id):
    pass

def Delete_Formas_de_pago(request, id):
    pass

def Delete_Viajeros(request, id):
    pass

def Delete_PAI_VIA(request, id):
    pass

def Delete_Registro_viajeros(request, id):
    pass

def Delete_Detalle_viajeros(request, id):
    pass

def Delete_Participantes(request, id):
    pass

def Delete_Puntuaciones(request, id):
    pass

#Edit

def Edit_Bancos(request, id):
    pass

def Edit_Clientes(request, id):
    pass

def Edit_Areas_de_interes(request, id):
    pass

def Edit_Paises(request, id):
    pass

def Edit_Rallies(request, id):
    pass

def Edit_Premios(request, id):
    pass

def Edit_Ciudades(request, id):
    pass

def Edit_Atracciones(request, id):
    pass

def Edit_Circuitos(request, id):
    pass

def Edit_ATR_CIR(request, id):
    pass

def Edit_Agencia_de_viajes(request, id):
    pass

def Edit_AGE_AGE(request, id):
    pass

def Edit_Cupos(request, id):
    pass

def Edit_Registro_clientes(request, id):
    pass

def Edit_Alojamientos(request, id):
    pass

def Edit_Proveedores(request, id):
    pass

def Edit_PRO_AGE(request, id):
    pass

def Edit_Asesores_de_viajes(request, id):
    pass

def Edit_Paquetes(request, id):
    pass

def Edit_Especializaciones(request, id):
    pass

def Edit_Precios_paquetes(request, id):
    pass

def Edit_Calendarios_anuales(request, id):
    pass

def Edit_Descuentos(request, id):
    pass

def Edit_Intinerarios(request, id):
    pass

def Edit_ITN_ATR(request, id):
    pass

def Edit_Detalles_servicios(request, id):
    pass

def Edit_ALO_DET(request, id):
    pass

def Edit_Instrumentos_de_pago(request, id):
    pass

def Edit_Paquetes_contrato(request, id):
    pass

def Edit_Formas_de_pago(request, id):
    pass

def Edit_Viajeros(request, id):
    pass

def Edit_PAI_VIA(request, id):
    pass

def Edit_Registro_viajeros(request, id):
    pass

def Edit_Detalle_viajeros(request, id):
    pass

def Edit_Participantes(request, id):
    pass

def Edit_Puntuaciones(request, id):
    pass