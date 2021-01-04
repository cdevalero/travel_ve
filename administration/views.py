from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from datetime import timedelta
from .sql_functions import *

# SHOW ---------------------------------------------------------------------------------------------------------------

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

#ADD --------------------------------------------------------------------------------------------------------------------

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

        try:
            del form.errors['id_premio']    #-> eliminar error de duplicidad si existe 
        except:
            pass

        if form.is_valid():

            id_premio = form.data['id_premio']  #-> definir cada una de las variables para guardarlas
            id_rally = form.data['id_rally']
            posicion = form.data['posicion']
            descripcion_premio = form.data['descripcion_premio']

            #-> Validad, que exista la entrada si se usa multiple FK

            Crear_Premios(id_premio, id_rally, posicion, descripcion_premio) # -> form.save()

            return redirect ('Show_premios')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_premios')
    form = Form_Premios()
    return render(request, 'create_edit/AddPremios.html',{'form':form})

def Add_Ciudades(request): #FIX
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

def Add_Atracciones(request): #FIX
    if request.method == 'POST':
        form = Form_Atracciones(request.POST)
        if form.is_valid():

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Add_Atracciones')

            form.save()
            return redirect ('Show_Atracciones')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Atracciones')
    form = Form_Atracciones()
    return render(request, 'create_edit/AddAtracciones.html',{'form':form})

def Add_Circuitos(request): #FIX
    if request.method == 'POST':
        form = Form_Circuitos(request.POST)
        if form.is_valid():

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Add_Circuitos')

            form.save()
            return redirect ('Show_Circuitos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Circuitos')
    form = Form_Circuitos()
    return render(request, 'create_edit/AddCircuitos.html',{'form':form})

def Add_ATR_CIR(request): #FIX
    if request.method == 'POST':
        form = Form_ATR_CIR(request.POST)
        if form.is_valid():

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            id_atraccion = form.cleaned_data.get('id_atraccion')
            try:
                atraccion = Atracciones.objects.get(id_ciudad=id_ciudad, id_pais=id_pais, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Add_atr_cir')

            id_circuito = form.cleaned_data.get('id_circuito')
            id_rally_cir = form.cleaned_data.get('id_rally_cir')
            id_ciudad_cir = form.cleaned_data.get('id_ciudad_cir')
            id_pais_cir = form.cleaned_data.get('id_pais_cir')
            try:
                circuito = Circuitos.objects.get(orden_circuito=id_circuito, id_rally=id_rally_cir, id_ciudad=id_ciudad_cir, id_pais=id_pais_cir)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'Error, la estructura del circuito viola integridad')
                return redirect('Add_atr_cir')

            form.save()
            return redirect ('Show_atr_cir')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_atr_cir')
    form = Form_ATR_CIR()
    return render(request, 'create_edit/AddATR_CIR.html',{'form':form})

def Add_Agencia_de_viajes(request):
    if request.method == 'POST':
        form = Form_Agencia_de_viajes(request.POST)
        if form.is_valid():

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Add_Agencia_de_viajes')

            form.save()
            return redirect ('Show_Agencia_de_viajes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Agencia_de_viajes')
    form = Form_Agencia_de_viajes()
    return render(request, 'create_edit/AddAgencia_de_viajes.html',{'form':form})

def Add_AGE_AGE(request): #FIX
    if request.method == 'POST':
        form = Form_AGE_AGE(request.POST)
        if form.is_valid():

            id_agencia = form.cleaned_data.get('id_agencia')
            id_socio = form.cleaned_data.get('id_socio')
            try:
                ciudad = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'No existe la agencia')
                return redirect('Add_AGE_AGE')
            try:
                ciudad = Agencias_de_viajes.objects.get(id_agencia=id_socio)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'No existe el socio')
                return redirect('Add_AGE_AGE')

            form.save()
            return redirect ('Show_AGE_AGE')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_AGE_AGE')
    form = Form_AGE_AGE()
    return render(request, 'create_edit/AddAGE_AGE.html',{'form':form})

def Add_Cupos(request): #FIX
    if request.method == 'POST':
        form = Form_Cupos(request.POST)
        if form.is_valid():

            id_agencia = form.cleaned_data.get('id_agencia')
            try:
                validacion = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'No existe la agencia')
                return redirect('Add_Cupos')

            form.save()
            return redirect ('Show_Cupos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Cupos')
    form = Form_Cupos()
    return render(request, 'create_edit/AddCupos.html',{'form':form})
        
def Add_Registro_clientes(request): #GUIA------------
    if request.method == 'POST':
        form = Form_Registro_clientes(request.POST)
        try:
            del form.errors['id_cliente']
        except:
            pass
        if form.is_valid():
            id_cliente = form.data['id_cliente']
            id_agencia = form.data['id_agencia']
            f_registro = form.data['f_registro']
            numero_registro = form.data['numero_registro']
            try:
                validacion = Clientes.objects.get(doc_identidad_o_rif=id_cliente)
            except Clientes.DoesNotExist:        
                messages.error(request, 'No existe el cliente')
                return redirect('Add_Registro_clientes')
            Crear_Registro_clientes(id_cliente, id_agencia, f_registro, numero_registro)
            #form.save()
            return redirect ('Show_Registro_clientes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Registro_clientes')
    form = Form_Registro_clientes()
    return render(request, 'create_edit/AddRegistro_clientes.html',{'form':form})

def Add_Alojamientos(request):
    if request.method == 'POST':
        form = Form_Alojamientos(request.POST)
        if form.is_valid():

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Add_Alojamientos')

            form.save()
            return redirect ('Show_Alojamientos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Alojamientos')
    form = Form_Alojamientos()
    return render(request, 'create_edit/AddAlojamientos.html',{'form':form})

def Add_Proveedores(request):
    if request.method == 'POST':
        form = Form_Proveedores(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_Proveedores')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Proveedores')
    form = Form_Proveedores()
    return render(request, 'create_edit/AddProveedores.html',{'form':form})

def Add_PRO_AGE(request): #FIX
    if request.method == 'POST':
        form = Form_PRO_AGE(request.POST)
        if form.is_valid():

            id_agencia = form.cleaned_data.get('id_agencia')
            try:
                validacion = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'No existe la agencia')
                return redirect('Add_pro_age')

            form.save()
            return redirect ('Show_pro_age')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_pro_age')
    form = Form_PRO_AGE()
    return render(request, 'create_edit/AddPRO_AGE.html',{'form':form})

def Add_Asesores_de_viajes(request):
    if request.method == 'POST':
        form = Form_Asesores_de_viajes(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_Asesores_de_viajes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Asesores_de_viajes')
    form = Form_Asesores_de_viajes()
    return render(request, 'create_edit/AddAsesores_de_viajes.html',{'form':form})

def Add_Paquetes(request): #FIX
    if request.method == 'POST':
        form = Form_Paquetes(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_Paquetes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Paquetes')
    form = Form_Paquetes()
    return render(request, 'create_edit/AddPaquetes.html',{'form':form})

def Add_Especializaciones(request): #FIX
    if request.method == 'POST':
        form = Form_Especializaciones(request.POST)
        if form.is_valid():

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            id_atraccion = form.cleaned_data.get('id_atraccion')
            try:
                validacion = Atracciones.objects.get(id_ciudad=id_ciudad, id_pais=id_pais, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Add_Especializaciones')
            
            id_paquete = form.cleaned_data.get('id_paquete')
            id_agencia_paquete = form.cleaned_data.get('id_agencia_paquete')
            try:
                validacion = Paquetes.objects.get(id_paquete=id_paquete, id_agencia=id_agencia_paquete)
            except Paquetes.DoesNotExist:        
                messages.error(request, 'Error, el paquete no pertenece a la agencia')
                return redirect('Add_Especializaciones')

            form.save()
            return redirect ('Show_Especializaciones')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Especializaciones')
    form = Form_Especializaciones()
    return render(request, 'create_edit/AddEspecializaciones.html',{'form':form})

def Add_Precios_paquetes(request): #FIX
    if request.method == 'POST':
        form = Form_Precios_paquetes(request.POST)
        if form.is_valid():

            id_paquete = form.cleaned_data.get('id_paquete')
            id_agencia = form.cleaned_data.get('id_agencia')
            try:
                validacion = Paquetes.objects.get(id_paquete=id_paquete, id_agencia=id_agencia)
            except Paquetes.DoesNotExist:        
                messages.error(request, 'Error, el paquete no pertenece a la agencia')
                return redirect('Add_Precios_paquetes')

            form.save()
            return redirect ('Show_Precios_paquetes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Precios_paquetes')
    form = Form_Precios_paquetes()
    return render(request, 'create_edit/AddPrecios_paquetes.html',{'form':form})

def Add_Calendarios_anuales(request): #FIX
    if request.method == 'POST':
        form = Form_Calendarios_anuales(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_Calendarios_anuales')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Calendarios_anuales')
    form = Form_Calendarios_anuales()
    return render(request, 'create_edit/AddCalendarios_anuales.html',{'form':form})

def Add_Descuentos(request): #FIX
    if request.method == 'POST':
        form = Form_Descuentos(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('Show_Descuentos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Descuentos')
    form = Form_Descuentos()
    return render(request, 'create_edit/AddDescuentos.html',{'form':form})

def Add_Intinerarios(request): #FIX
    if request.method == 'POST':
        form = Form_Itinerarios(request.POST)
        if form.is_valid():

            id_paquete = form.cleaned_data.get('id_paquete')
            id_agencia = form.cleaned_data.get('id_agencia')
            try:
                validacion = Paquetes.objects.get(id_paquete=id_paquete, id_agencia=id_agencia)
            except Paquetes.DoesNotExist:        
                messages.error(request, 'Error, el paquete no pertenece a la agencia')
                return redirect('Add_Intinerarios')

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Add_Intinerarios')

            form.save()
            return redirect ('Show_Intinerarios')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Intinerarios')
    form = Form_Itinerarios()
    return render(request, 'create_edit/AddIntinerarios.html',{'form':form})

def Add_ITN_ATR(request): #FIX
    if request.method == 'POST':
        form = Form_ITN_ATR(request.POST)
        if form.is_valid():

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            id_atraccion = form.cleaned_data.get('id_atraccion')
            try:
                validacion = Atracciones.objects.get(id_ciudad=id_ciudad, id_pais=id_pais, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Add_ITN_ATR')

            id_itinerario = form.cleaned_data.get('id_itinerario')
            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            id_agencia = form.cleaned_data.get('id_agencia')
            id_paquete = form.cleaned_data.get('id_paquete')
            try:
                validacion = Itinerarios.objects.get(orden=id_itinerario, id_ciudad=id_ciudad, id_pais=id_pais, id_agencia=id_agencia, id_paquete=id_paquete)
            except Itinerarios.DoesNotExist:        
                messages.error(request, 'Error con la union de itinerario, ciudad, pais, agencia, paquete')
                return redirect('Add_ITN_ATR')

            form.save()
            return redirect ('Show_ITN_ATR')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_ITN_ATR')
    form = Form_ITN_ATR()
    return render(request, 'create_edit/AddITN_ATR.html',{'form':form})

def Add_Detalles_servicios(request): #FIX
    if request.method == 'POST':
        form = Form_Detalles_servicios(request.POST)
        if form.is_valid():

            id_itinerario = form.cleaned_data.get('id_itinerario')
            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            id_agencia = form.cleaned_data.get('id_agencia')
            id_paquete = form.cleaned_data.get('id_paquete')
            try:
                validacion = Itinerarios.objects.get(orden=id_itinerario, id_ciudad=id_ciudad, id_pais=id_pais, id_agencia=id_agencia, id_paquete=id_paquete)
            except Itinerarios.DoesNotExist:        
                messages.error(request, 'Error con la union de itinerario, ciudad, pais, agencia, paquete')
                return redirect('Add_Detalles_servicios')

            form.save()
            return redirect ('Show_Detalles_servicios')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Detalles_servicios')
    form = Form_Detalles_servicios()
    return render(request, 'create_edit/AddDetalles_servicios.html',{'form':form})

def Add_ALO_DET(request): #FIX
    if request.method == 'POST':
        form = Form_ALO_DET(request.POST)
        if form.is_valid():

            id_detalle_servicio = form.cleaned_data.get('id_detalle_servicio')
            id_itinerario = form.cleaned_data.get('id_itinerario')
            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            id_agencia = form.cleaned_data.get('id_agencia')
            id_paquete = form.cleaned_data.get('id_paquete')
            try:
                validacion = Detalles_servicios.objects.get(id_detalle_servicio=id_detalle_servicio, orden=id_itinerario, id_ciudad=id_ciudad, id_pais=id_pais, id_agencia=id_agencia, id_paquete=id_paquete)
            except Detalles_servicios.DoesNotExist:        
                messages.error(request, 'Error con la union de itinerario, ciudad, pais, agencia, paquete y detalle servicio')
                return redirect('Add_ALO_DET')


            form.save()
            return redirect ('Show_ALO_DET')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_ALO_DET')
    form = Form_ALO_DET()
    return render(request, 'create_edit/AddALO_DET.html',{'form':form})

def Add_Instrumentos_de_pago(request): #FIX
    if request.method == 'POST':
        form = Form_Instrumentos_de_pago(request.POST)
        if form.is_valid():

            doc_identidad_cliente = form.cleaned_data.get('doc_identidad_cliente')
            try:
                validacion = Clientes.objects.get(doc_identidad_o_rif=doc_identidad_cliente)
            except Clientes.DoesNotExist:        
                messages.error(request, 'Cliente no existe')
                return redirect('Add_Instrumentos_de_pago')

            form.save()
            return redirect ('Show_Instrumentos_de_pago')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Instrumentos_de_pago')
    form = Form_Instrumentos_de_pago()
    return render(request, 'create_edit/AddInstrumentos_de_pago.html',{'form':form})

def Add_Paquetes_contrato(request):
    if request.method == 'POST':
        form = Form_Paquetes_contrato(request.POST)
        if form.is_valid():

            id_paquete = form.cleaned_data.get('id_paquete')
            id_agencia = form.cleaned_data.get('id_agencia')
            try:
                validacion = Paquetes.objects.get(id_paquete=id_paquete, id_agencia=id_agencia)
            except Paquetes.DoesNotExist:        
                messages.error(request, 'Error, el paquete no pertenece a la agencia')
                return redirect('Add_Paquetes_contrato')

            id_reg_cliente = form.cleaned_data.get('id_reg_cliente')
            id_reg_agencia = form.cleaned_data.get('id_reg_agencia')
            try:
                validacion = Registro_clientes.objects.get(id_cliente=id_reg_cliente, id_agencia=id_reg_agencia)
            except Paquetes.DoesNotExist:        
                messages.error(request, 'Error, el paquete no pertenece a la agencia')
                return redirect('Add_Paquetes_contrato')

            form.save()
            return redirect ('Show_Paquetes_contrato')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Paquetes_contrato')
    form = Form_Paquetes_contrato()
    return render(request, 'create_edit/AddPaquetes_contrato.html',{'form':form})

def Add_Formas_de_pago(request): #FIX
    if request.method == 'POST':
        form = Form_Formas_de_pago(request.POST)
        if form.is_valid():

            id_instrumento = form.cleaned_data.get('id_instrumento')
            id_cliente = form.cleaned_data.get('id_cliente')
            try:
                validacion = Instrumentos_de_pago.objects.get(id_instrumento=id_instrumento, doc_identidad_cliente=id_cliente)
            except Instrumentos_de_pago.DoesNotExist:        
                messages.error(request, 'Error, instrumento de pago y cliente no coinciden')
                return redirect('Add_Formas_de_pago')

            id_paquete_contrato = form.cleaned_data.get('id_paquete_contrato')
            try:
                validacion = Paquetes_contrato.objects.get(numero_factura=id_paquete_contrato)
            except Paquetes_contrato.DoesNotExist:        
                messages.error(request, 'Error, paquete contrato invalido')
                return redirect('Add_Formas_de_pago')

            form.save()
            return redirect ('Show_Formas_de_pago')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Formas_de_pago')
    form = Form_Formas_de_pago()
    return render(request, 'create_edit/AddFormas_de_pago.html',{'form':form})

def Add_Viajeros(request):
    if request.method == 'POST':
        form = Form_Viajeros(request.POST)
        if form.is_valid():

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Add_Viajeros')

            id_paquete_contrato = form.cleaned_data.get('id_paquete_contrato')
            try:
                validacion = Paquetes_contrato.objects.get(numero_factura=id_paquete_contrato)
            except Paquetes_contrato.DoesNotExist:        
                messages.error(request, 'Error, paquete contrato invalido')
                return redirect('Add_Viajeros')

            form.save()
            return redirect ('Show_Viajeros')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Viajeros')
    form = Form_Viajeros()
    return render(request, 'create_edit/AddViajeros.html',{'form':form})

def Add_PAI_VIA(request):#FIX
    if request.method == 'POST':
        form = Form_PAI_VIA(request.POST)
        if form.is_valid():

            id_viajero = form.cleaned_data.get('id_viajero')
            try:
                validacion = Viajeros.objects.get(id_de_identidad=id_viajero)
            except Viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero invalido')
                return redirect('Add_PAI_VIA')

            form.save()
            return redirect ('Show_PAI_VIA')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_PAI_VIA')
    form = Form_PAI_VIA()
    return render(request, 'create_edit/AddPAI_VIA.html',{'form':form})

def Add_Registro_viajeros(request): #FIX
    if request.method == 'POST':
        form = Form_Registro_viajeros(request.POST)
        if form.is_valid():

            id_viajero = form.cleaned_data.get('id_viajero')
            try:
                validacion = Viajeros.objects.get(id_de_identidad=id_viajero)
            except Viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero invalido')
                return redirect('Add_Registro_viajeros')

            id_agencia = form.cleaned_data.get('id_agencia')
            try:
                validacion = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'Error, Agencia invalida')
                return redirect('Add_Registro_viajeros')

            form.save()
            return redirect ('Show_Registro_viajeros')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Registro_viajeros')
    form = Form_Registro_viajeros()
    return render(request, 'create_edit/AddRegistro_viajeros.html',{'form':form})

def Add_Detalle_viajeros(request): #FIX
    if request.method == 'POST':
        form = Form_Detalle_viajeros(request.POST)
        if form.is_valid():

            id_viajero = form.cleaned_data.get('id_viajero')
            id_agencia = form.cleaned_data.get('id_agencia')
            try:
                validacion = Registro_viajeros.objects.get(id_agencia=id_agencia, id_viajero=id_viajero)
            except Registro_viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero no pertenece a la agencia')
                return redirect('Add_Detalle_viajeros')

            id_paquete_contrato = form.cleaned_data.get('id_paquete_contrato')
            try:
                validacion = Paquetes_contrato.objects.get(numero_factura=id_paquete_contrato)
            except Paquetes_contrato.DoesNotExist:        
                messages.error(request, 'Error, Paquete invalido')
                return redirect('Add_Detalle_viajeros')

            form.save()
            return redirect ('Show_Detalle_viajeros')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Detalle_viajeros')
    form = Form_Detalle_viajeros()
    return render(request, 'create_edit/AddDetalle_viajeros.html',{'form':form})

def Add_Participantes(request): #FIX
    if request.method == 'POST':
        form = Form_Participantes(request.POST)
        if form.is_valid():

            id_via_viajero = form.cleaned_data.get('id_via_viajero')
            id_via_agencia = form.cleaned_data.get('id_agencia')
            try:
                validacion = Registro_viajeros.objects.get(id_agencia=id_via_agencia, id_viajero=id_via_viajero)
            except Registro_viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero no pertenece a la agencia')
                return redirect('Add_Participantes')

            id_cli_cliente = form.cleaned_data.get('id_cli_cliente')
            id_cli_agencia = form.cleaned_data.get('id_agencia')
            try:
                validacion = Registro_viajeros.objects.get(id_cliente=id_cli_cliente, id_agencia=id_cli_agencia)
            except Registro_clientes.DoesNotExist:        
                messages.error(request, 'Error, Cliente no pertenece a la agencia')
                return redirect('Add_Participantes')

            form.save()
            return redirect ('Show_Participantes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Participantes')
    form = Form_Participantes()
    return render(request, 'create_edit/AddParticipantes.html',{'form':form})

def Add_Puntuaciones(request):
    if request.method == 'POST':
        form = Form_Puntuaciones(request.POST)
        if form.is_valid():

            id_paquete_contrato = form.cleaned_data.get('id_paquete_contrato')
            try:
                validacion = Paquetes_contrato.objects.get(numero_factura=id_paquete_contrato)
            except Paquetes_contrato.DoesNotExist:        
                messages.error(request, 'Error, paquete contrato invalido')
                return redirect('Add_Puntuaciones')

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            id_atraccion = form.cleaned_data.get('id_atraccion')
            try:
                atraccion = Atracciones.objects.get(id_ciudad=id_ciudad, id_pais=id_pais, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Add_Puntuaciones')

            form.save()
            return redirect ('Show_Puntuaciones')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Puntuaciones')
    form = Form_Puntuaciones()
    return render(request, 'create_edit/AddPuntuaciones.html',{'form':form})


#Delete ------------------------------------------------------------------------------------------------------------

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
        obj = Premios.objects.filter(id_rally=rallie.id_rally).get(id_premio=id)
    except Premios.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_rallies')
    Borrar_Premios(id, rallie.id_rally)
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
    Borrar_Ciudad(id, pais.id_pais)
    return redirect('Show_Ciudades')

def Delete_Atracciones(request, id,id2,id3):
    try:
        ciudad = Ciudades.objects.get(id_ciudad=id2)
    except Ciudades.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Atracciones')
    try:
        pais = Paises.objects.get(id_pais=id3)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Atracciones')
    try:
        obj = Atracciones.objects.filter(id_ciudad=ciudad.id_ciudad,id_pais=pais.id_pais).get(id_atraccion=id)
    except Atracciones.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Atracciones')
    Borrar_Atraccion(id, ciudad.id_ciudad, pais.id_pais)
    return redirect('Show_Atracciones')

def Delete_Circuitos(request, id,id2,id3,id4):
    try:
        ciudad = Ciudades.objects.get(id_ciudad=id3)
    except Ciudades.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Circuitos')
    try:
        pais = Paises.objects.get(id_pais=id4)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Circuitos')
    try:
        rallie = Rallies.objects.get(nombre_rally=id2)
    except Rallies.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_Circuitos')
    try:
        obj = Circuitos.objects.filter(id_ciudad=ciudad.id_ciudad,id_pais=pais.id_pais,id_rally=rallie.id_rally).get(orden_circuito=id)
    except Circuitos.DoesNotExist:        
        messages.error(request, 'No existe la 4')
        return redirect('Show_Circuitos')
    Borrar_Circuito(id, rallie.id_rally, ciudad.id_ciudad, pais.id_pais)
    return redirect('Show_Circuitos')  

def Delete_ATR_CIR(request, id,id2,id3,id4,id5,id6,id7):
    try:
        atraccion = Atracciones.objects.get(id_atraccion=id)
    except Atracciones.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_atr_cir')
    try:
        ciudad_at = Ciudades.objects.get(id_ciudad=id2)
    except Ciudades.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_atr_cir')
    try:
        pais_at = Paises.objects.get(id_pais=id3)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_atr_cir')
    try:
        circuito = Circuitos.objects.get(orden_circuito=id4)
    except Circuitos.DoesNotExist:        
        messages.error(request, 'No existe la entrada4')
        return redirect('Show_atr_cir')
    try:
        rallie = Rallies.objects.get(id_rally=id5)
    except Rallies.DoesNotExist:        
        messages.error(request, 'No existe la entrada5')
        return redirect('Show_atr_cir')
    try:
        ciudad_cir = Ciudades.objects.get(id_ciudad=id6)
    except Ciudades.DoesNotExist:        
        messages.error(request, 'No existe la entrada6')
        return redirect('Show_atr_cir')
    try:
        pais_cir = Paises.objects.get(id_pais=id7)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada7')
        return redirect('Show_atr_cir')
    try:
        obj = ATR_CIR.objects.filter(id_ciudad_at=ciudad_at.id_ciudad,id_pais_at=pais_at.id_pais,id_circuito=circuito.orden_circuito,id_rally_cir=rallie.id_rally,id_ciudad_cir=ciudad_at.id_ciudad,id_pais_cir=pais_at.id_pais).get(id_atraccion=id)
    except ATR_CIR.DoesNotExist:        
        messages.error(request, 'No existe la entrada8')
        return redirect('Show_atr_cir')
    Borrar_ATR_CIR(atraccion.id_atraccion, ciudad_at.id_ciudad, pais_at.id_pais, circuito.orden_circuito, rallie.id_rally, ciudad_at.id_ciudad, pais_at.id_pais)
    return redirect('Show_atr_cir')

def Delete_Agencia_de_viajes(request, id):
    try:
        obj = Agencias_de_viajes.objects.get(pk=id)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Agencia_de_viajes')
    obj.delete()
    return redirect('Show_Agencia_de_viajes')

def Delete_AGE_AGE(request, id,id2):
    try:
        socio = Agencias_de_viajes.objects.get(id_agencia=id2)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_AGE_AGE')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_AGE_AGE')
    try:
        obj = AGE_AGE.objects.filter(id_socio=socio.id_agencia).get(id_agencia=id)
    except AGE_AGE.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_AGE_AGE')
    Borrar_AGE_AGE(id, socio.id_agencia)
    return redirect('Show_AGE_AGE')

def Delete_Cupos(request, id, id2):
    try:
        rallie = Rallies.objects.get(nombre_rally=id2)
    except Rallies.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Cupos')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Cupos')
    try:
        obj = Cupos.objects.filter(id_rally=rallie.id_rally).get(id_agencia=id)
    except Cupos.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_Cupos')
    Borrar_Cupo(id, rallie.id_rally)
    return redirect('Show_Cupos')

def Delete_Registro_clientes(request, id,id2):
    try:
        cliente = Clientes.objects.get(doc_identidad_o_rif=id)
    except Clientes.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Registro_clientes')
    try:
        agencia = Agencias_de_viajes.objects.get(nombre=id2)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Registro_clientes')
    try:
        obj = Registro_clientes.objects.filter(id_agencia=agencia.id_agencia).get(id_cliente=cliente.doc_identidad_o_rif)
    except Registro_clientes.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_Registro_clientes')
    Borrar_Registro_clientes(id, agencia.id_agencia)
    return redirect('Show_Registro_clientes')

def Delete_Alojamientos(request, id):
    try:
        obj = Alojamientos.objects.get(pk=id)
    except Alojamientos.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Alojamientos')
    obj.delete()
    return redirect('Show_Alojamientos')

def Delete_Proveedores(request, id):
    try:
        obj = Proveedores.objects.get(pk=id)
    except Proveedores.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Proveedores')
    obj.delete()
    return redirect('Show_Proveedores')

def Delete_PRO_AGE(request, id,id2):
    try:
       proveedor = Proveedores.objects.get(nombre_proveedor=id2)
    except Proveedores.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_pro_age')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_pro_age')
    try:
        obj = PRO_AGE.objects.filter(id_proveedor=proveedor.id_proveedor).get(id_agencia=id)
    except PRO_AGE.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_pro_age')
    Borrar_PRO_AGE(id, proveedor.id_proveedor)
    return redirect('Show_pro_age')

def Delete_Asesores_de_viajes(request, id):
    try:
        obj = Asesores_de_viajes.objects.get(pk=id)
    except Asesores_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Asesores_de_viajes')
    obj.delete()
    return redirect('Show_Asesores_de_viajes')

def Delete_Paquetes(request, id,id2):
    try:
       paquete = Paquetes.objects.get(id_paquete=id)
    except Paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Paquetes')
    try:
        agencia = Agencias_de_viajes.objects.get(nombre=id2)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Paquetes')
    try:
        obj = Paquetes.objects.filter(id_agencia=agencia.id_agencia).get(id_paquete=id)
    except Paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_Paquetes')
    Borrar_Paquetes(id, agencia.id_agencia)
    return redirect('Show_Paquetes')

def Delete_Especializaciones(request, id,id2):
    try:
       especializacion = Especializaciones.objects.get(id_especializacion=id)
    except Especializaciones.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Especializaciones')
    try:
        area = Areas_de_interes.objects.get(nombre_area_de_interes=id2)
    except Areas_de_interes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Especializaciones')
    try:
        obj = Especializaciones.objects.filter(id_areas_de_interes=area.id_areas_de_interes).get(id_especializacion=id)
    except Especializaciones.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_Especializaciones')
    Borrar_Especializacion(id, area.id_areas_de_interes)
    return redirect('Show_Especializaciones')

def Delete_Precios_paquetes(request, id,id2,id3):
    try:
       paquete = Paquetes.objects.get(id_paquete=id2)
    except Paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Precios_paquetes')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id3)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Precios_paquetes')
    try:
        obj = Precios_paquetes.objects.filter( id_paquete=paquete.id_paquete,id_agencia=agencia.id_agencia).get(f_inicio=id)
    except Precios_paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_Precios_paquetes')
    Borrar_Precio_paquete(id,paquete.id_paquete, agencia.id_agencia)
    return redirect('Show_Precios_paquetes')

def Delete_Calendarios_anuales(request, id,id2,id3):
    try:
       paquete = Paquetes.objects.get(id_paquete=id2)
    except Paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Calendarios_anuales')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id3)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Calendarios_anuales')
    try:
        obj = Calendarios_anuales.objects.filter( id_paquete=paquete.id_paquete,id_agencia=agencia.id_agencia).get(f_salida=id)
    except Precios_paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_Calendarios_anuales')
    Borrar_Calendarios_anuales(id, paquete.id_paquete, agencia.id_agencia)
    return redirect('Show_Calendarios_anuales')

def Delete_Descuentos(request, id,id2):
    try:
        agencia = Agencias_de_viajes.objects.get(nombre=id2)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Descuentos')
    try:
        obj = Descuentos.objects.filter( id_agencia=agencia.id_agencia).get(id_descuento=id)
    except Precios_paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Descuentos')
    Borrar_Descuentos(id, agencia.id_agencia)
    return redirect('Show_Descuentos')

def Delete_Intinerarios(request, id,id2,id3,id4,id5):
    try:
       paquete = Paquetes.objects.get(id_paquete=id2)
    except Paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Intinerarios')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id3)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Intinerarios')
    try:
        ciudad = Ciudades.objects.get(id_ciudad=id4)
    except Ciudades.DoesNotExist:        
        messages.error(request, 'No existe la entrada6')
        return redirect('Show_Intinerarios')
    try:
        pais = Paises.objects.get(id_pais=id5)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada7')
        return redirect('Show_Intinerarios')
    try:
        obj = Itinerarios.objects.filter( id_paquete=paquete.id_paquete,id_agencia=agencia.id_agencia,id_ciudad=ciudad.id_ciudad,id_pais=pais.id_pais).get(orden=id)
    except Itinerarios.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Intinerarios')
    Borrar_Itinerarios(id, ciudad.id_ciudad, pais.id_pais, agencia.id_agencia, paquete.id_paquete)
    return redirect('Show_Intinerarios')

def Delete_ITN_ATR(request, id,id2,id3,id4,id5,id6,id7,id8):
    try:
        itinerario = Itinerarios.objects.get(orden=id)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_ITN_ATR')
    try:
        atraccion = Atracciones.objects.get(id_atraccion=id6)
    except Atracciones.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_ITN_ATR')
    try:
        ciudad_at = Ciudades.objects.get(id_ciudad=id7)
    except Ciudades.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_ITN_ATR')
    try:
        pais_at = Paises.objects.get(id_pais=id8)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada4')
        return redirect('Show_ITN_ATR')
    try:
       paquete = Paquetes.objects.get(id_paquete=id2)
    except Paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada5')
        return redirect('Show_ITN_ATR')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id3)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada6')
        return redirect('Show_ITN_ATR')
    try:
        ciudad = Ciudades.objects.get(id_ciudad=id4)
    except Ciudades.DoesNotExist:        
        messages.error(request, 'No existe la entrada7')
        return redirect('Show_ITN_ATR')
    try:
        pais = Paises.objects.get(id_pais=id5)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada8')
        return redirect('Show_ITN_ATR')
    try:
        obj = ITN_ATR.objects.filter(id_itinerario=itinerario.orden,id_paquete=paquete.id_paquete,id_agencia=agencia.id_agencia,id_ciudad=ciudad.id_ciudad,id_pais=pais.id_pais,id_atraccion=atraccion.id_atraccion,id_ciudad_at=ciudad_at.id_ciudad,id_pais_at=pais_at.id_pais).get(id_itinerario=id)
    except ITN_ATR.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_ITN_ATR')
    Borrar_ITN_ATR(id, ciudad.id_ciudad, pais.id_pais, agencia.id_agencia, paquete.id_paquete, atraccion.id_atraccion, ciudad_at.id_ciudad, pais_at.id_pais)
    return redirect('Show_ITN_ATR')

def Delete_Detalles_servicios(request, id,id2,id3,id4,id5,id6):
    try:
        itinerario = Itinerarios.objects.get(orden=id2)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Detalles_servicios')
    try:
       paquete = Paquetes.objects.get(id_paquete=id3)
    except Paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Detalles_servicios')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id4)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_Detalles_servicios')
    try:
        ciudad = Ciudades.objects.get(id_ciudad=id5)
    except Ciudades.DoesNotExist:        
        messages.error(request, 'No existe la entrada4')
        return redirect('Show_Detalles_servicios')
    try:
        pais = Paises.objects.get(id_pais=id6)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada5')
        return redirect('Show_Detalles_servicios')
    try:
        obj = Detalles_servicios.objects.filter(id_itinerario=itinerario.orden,id_paquete=paquete.id_paquete,id_agencia=agencia.id_agencia,id_ciudad=ciudad.id_ciudad,id_pais=pais.id_pais).get(id_detalle_servicio=id)
    except Detalles_servicios.DoesNotExist:        
        messages.error(request, 'No existe la entrada6')
        return redirect('Show_Detalles_servicios')
    Borrar_Detalle_servicio(id, itinerario.orden, paquete.id_paquete, agencia.id_agencia, ciudad.id_ciudad, pais.id_pais)
    return redirect('Show_Detalles_servicios')

def Delete_ALO_DET(request, id,id2,id3,id4,id5,id6,id7):
    try:
        detalle = Detalles_servicios.objects.get(id_detalle_servicio=id)
    except Detalles_servicios.DoesNotExist:        
        messages.error(request, 'No existe la entrada5')
        return redirect('Show_ALO_DET')
    try:
        itinerario = Itinerarios.objects.get(orden=id2)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_ALO_DET')
    try:
       paquete = Paquetes.objects.get(id_paquete=id3)
    except Paquetes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_ALO_DET')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id4)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_ALO_DET')
    try:
        ciudad = Ciudades.objects.get(id_ciudad=id5)
    except Ciudades.DoesNotExist:        
        messages.error(request, 'No existe la entrada4')
        return redirect('Show_ALO_DET')
    try:
        pais = Paises.objects.get(id_pais=id6)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada5')
        return redirect('Show_ALO_DET')
    try:
        alojamiento = Alojamientos.objects.get(id_alojamiento=id7)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada5')
        return redirect('Show_ALO_DET')
    try:
        obj = ALO_DET.objects.filter(id_detalle_servicio=detalle.id_detalle_servicio,id_itinerario=itinerario.orden,id_paquete=paquete.id_paquete,id_agencia=agencia.id_agencia,id_ciudad=ciudad.id_ciudad,id_pais=pais.id_pais,id_alojamiento=alojamiento.id_alojamiento).get(id_detalle_servicio=id)
    except ALO_DET.DoesNotExist:        
        messages.error(request, 'No existe la entrada6')
        return redirect('Show_ALO_DET')
    Borrar_ALO_DET(id, itinerario.orden, paquete.id_paquete, agencia.id_agencia, ciudad.id_ciudad, pais.id_pais, alojamiento.id_alojamiento)
    return redirect('Show_ALO_DET')

def Delete_Instrumentos_de_pago(request, id,id2):
    try:
        cliente = Clientes.objects.get(doc_identidad_o_rif=id2)
    except Clientes.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Instrumentos_de_pago')
    try:
        obj = Instrumentos_de_pago.objects.filter(doc_identidad_cliente=cliente.doc_identidad_o_rif).get(id_instrumento=id)
    except Instrumentos_de_pago.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Instrumentos_de_pago')
    Borrar_Instrumento_de_pago(id, cliente.doc_identidad_o_rif)
    return redirect('Show_Instrumentos_de_pago')

def Delete_Paquetes_contrato(request, id):
    try:
        obj = Paquetes_contrato.objects.get(pk=id)
    except Paquetes_contrato.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Paquetes_contrato')
    obj.delete()
    return redirect('Show_Paquetes_contrato')

def Delete_Formas_de_pago(request, id,id2,id3):
    try:
        instrumentos = Instrumentos_de_pago.objects.get(id_instrumento=id)
    except Instrumentos_de_pago.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Formas_de_pago')
    try:
        cliente = Clientes.objects.get(doc_identidad_o_rif=id2)
    except Clientes.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Formas_de_pago')
    try:
        paq_cont = Paquetes_contrato.objects.get(numero_factura=id3)
    except Paquetes_contrato.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Formas_de_pago')
    try:
        obj = Formas_de_pago.objects.filter(id_instrumento=instrumentos.id_instrumento,id_cliente=cliente.doc_identidad_o_rif,id_paquete_contrato=paq_cont.numero_factura).get(id_instrumento=id)
    except Formas_de_pago.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Formas_de_pago')
    Borrar_Forma_de_pago(id, cliente.doc_identidad_o_rif, paq_cont.numero_factura)
    return redirect('Show_Formas_de_pago')

def Delete_Viajeros(request, id):
    try:
        obj =Viajeros.objects.get(pk=id)
    except Viajeros.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Viajeros')
    obj.delete()
    return redirect('Show_Viajeros')

def Delete_PAI_VIA(request, id,id2):
    try:
        viajero = Viajeros.objects.get(id_de_identidad=id)
    except Viajeros.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_PAI_VIA')
    try:
        pais = Paises.objects.get(nombre_pais=id2)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada7')
        return redirect('Show_PAI_VIA')
    try:
        obj = PAI_VIA.objects.filter(id_viajero=viajero.id_de_identidad,id_pais=pais.id_pais).get(id_viajero=id)
    except PAI_VIA.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_PAI_VIA')
    Borrar_PAI_VIA(id, pais.id_pais)
    return redirect('Show_PAI_VIA')

def Delete_Registro_viajeros(request, id,id2):
    try:
        viajero = Viajeros.objects.get(id_de_identidad=id2)
    except Viajeros.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Registro_viajeros')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_Registro_viajeros')
    try:
        obj = Registro_viajeros.objects.filter(id_viajero=viajero.id_de_identidad,id_agencia=agencia.id_agencia).get(id_viajero=id2)
    except Registro_viajeros.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Registro_viajeros')
    Borrar_Registro_viajeros(agencia.id_agencia, viajero.id_de_identidad)
    return redirect('Show_Registro_viajeros')

def Delete_Detalle_viajeros(request, id,id2,id3):
    try:
        viajero = Viajeros.objects.get(id_de_identidad=id)
    except Viajeros.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Detalle_viajeros')
    try:
        agencia = Agencias_de_viajes.objects.get(id_agencia=id2)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Detalle_viajeros')
    try:
        paq_cont = Paquetes_contrato.objects.get(numero_factura=id3)
    except Paquetes_contrato.DoesNotExist:        
        messages.error(request, 'No existe la entrada3')
        return redirect('Show_Detalle_viajeros')
    try:
        obj = Detalle_viajeros.objects.filter(id_viajero=viajero.id_de_identidad,id_agencia=agencia.id_agencia,id_paquete_contrato=paq_cont.numero_factura).get(id_viajero=id)
    except Detalle_viajeros.DoesNotExist:        
        messages.error(request, 'No existe la entrada4')
        return redirect('Show_Detalle_viajeros')
    Borrar_Detalle_viajero(id, agencia.id_agencia, paq_cont.numero_factura)
    return redirect('Show_Detalle_viajeros')

def Delete_Participantes(request, id,id2):
    try:
        rallie = Rallies.objects.get(nombre_rally=id2)
    except Rallies.DoesNotExist:        
        messages.error(request, 'No existe la entrada1')
        return redirect('Show_Participantes')
    try:
        obj = Participantes.objects.filter(id_rally=rallie.id_rally).get(id_partipante=id)
    except Participantes.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Participantes')
    Borrar_Participantes(id, rallie.id_rally)
    return redirect('Show_Participantes')

def Delete_Puntuaciones(request, id):
    try:
        obj = Puntuaciones.objects.get(id_puntuacion=id)
    except Puntuaciones.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Puntuaciones')
    obj.delete()
    return redirect('Show_Puntuaciones')

#Edit ------------------------------------------------------------------------------------------------------------------

def Edit_Bancos(request, id):

    try:
        obj = Bancos.objects.get(id_banco=id)
    except Bancos.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('Show_bancos')

    if request.method == 'POST':
        form = Form_Bancos(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect ('Show_bancos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_bancos')
    form = Form_Bancos(instance= obj)
    return render(request, 'create_edit/AddBancos.html',{'form':form})

def Edit_Clientes(request, id):

    try:
        obj = Clientes.objects.get(doc_identidad_o_rif=id)
    except Clientes.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Clientes')

    if request.method == 'POST':
        form = Form_Clientes(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect ('Show_Clientes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Clientes')
    form = Form_Clientes(instance= obj)
    return render(request, 'create_edit/AddClientes.html',{'form':form})

def Edit_Areas_de_interes(request, id):
    
    try:
        obj = Areas_de_interes.objects.get(id_areas_de_interes=id)
    except Areas_de_interes.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Areas_de_interes')

    if request.method == 'POST':
        form = Form_Areas_de_interes(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect ('Show_Areas_de_interes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Areas_de_interes')
    form = Form_Areas_de_interes(instance= obj)
    return render(request, 'create_edit/AddAreas_de_interes.html',{'form':form})

def Edit_Paises(request, id):
    
    try:
        obj = Paises.objects.get(id_pais=id)
    except Paises.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('Show_paises')

    if request.method == 'POST':
        form = Form_Paises(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect ('Show_paises')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_paises')
    form = Form_Paises(instance= obj)
    return render(request, 'create_edit/AddPaises.html',{'form':form})

def Edit_Rallies(request, id):

    try:
        obj = Rallies.objects.get(id_rally=id)
    except Rallies.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('Show_rallies')

    if request.method == 'POST':
        form = Form_Rallies(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect ('Show_rallies')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_rallies')
    form = Form_Rallies(instance= obj)
    return render(request, 'create_edit/AddRallies.html',{'form':form})

def Edit_Premios(request, id, id2):
    pass

def Edit_Ciudades(request, id, id2):
    pass

def Edit_Atracciones(request, id, id2, id3):
    pass

def Edit_Circuitos(request, id,id2,id3,id4):
    pass

def Edit_ATR_CIR(request, id,id2,id3,id4,id5,id6,id7):
    pass

def Edit_Agencia_de_viajes(request, id):
    pass

def Edit_AGE_AGE(request, id,id2):
    pass

def Edit_Cupos(request, id,id2):
    pass

def Edit_Registro_clientes(request, id,id2):
    pass

def Edit_Alojamientos(request, id):
    pass

def Edit_Proveedores(request, id):
    pass

def Edit_PRO_AGE(request, id,id2):
    pass

def Edit_Asesores_de_viajes(request, id):
    pass

def Edit_Paquetes(request, id,id2):
    pass

def Edit_Especializaciones(request, id,id2):
    pass

def Edit_Precios_paquetes(request, id,id2,id3):
    pass

def Edit_Calendarios_anuales(request, id,id2,id3):
    pass

def Edit_Descuentos(request, id,id2):
    pass

def Edit_Intinerarios(request, id,id2,id3,id4,id5):
    pass

def Edit_ITN_ATR(request, id,id2,id3,id4,id5,id6,id7,id8):
    pass

def Edit_Detalles_servicios(request, id,id2,id3,id4,id5,id6):
    pass

def Edit_ALO_DET(request, id,id2,id3,id4,id5,id6,id7):
    pass

def Edit_Instrumentos_de_pago(request, id,id2):
    pass

def Edit_Paquetes_contrato(request, id):
    pass

def Edit_Formas_de_pago(request, id,id2,id3):
    pass

def Edit_Viajeros(request, id):
    pass

def Edit_PAI_VIA(request, id,id2):
    pass

def Edit_Registro_viajeros(request, id,id2):
    pass

def Edit_Detalle_viajeros(request, id,id2,id3):
    pass

def Edit_Participantes(request, id,id2):
    pass

def Edit_Puntuaciones(request, id):
    pass