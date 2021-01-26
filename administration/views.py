from django.db.models.deletion import ProtectedError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from datetime import timedelta
from .sql_functions import *
from datetime import date

# SHOW -----------------------------------------------------------------------------------------------------------------------------------------

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

#ADD ------------------------------------------------------------------------------------------------------------------------------------------

def Add_Bancos(request):
    if request.method == 'POST':
        form = Form_Bancos(request.POST)
        if form.is_valid():
            nombre_banco = form.data['nombre_banco']   
            Crear_Banco(nombre_banco)
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
            nombre_pais = form.data['nombre_pais']  
            region_pais = form.data['region_pais']  
            continente_pais = form.data['continente_pais']  
            nacionalidad = form.data['nacionalidad']  
            descripcion_pais = form.data['descripcion_pais']  
            if region_pais == "EU" and continente_pais == "Europa":
                pass
            elif region_pais == "AF_MO" and continente_pais == "Africa":
                pass
            elif region_pais == "AF_MO" and continente_pais == "Asia":
                pass
            elif region_pais == "AU_NZ_PAC" and continente_pais == "Oceania":
                pass
            elif region_pais == "AS" and continente_pais == "Asia":
                pass
            elif region_pais == "MEX_CEN_SUR" and continente_pais == "America":
                pass
            elif region_pais == "USA_CAN_CAR" and continente_pais == "America":
                pass
            else:
                messages.error(request, 'El continento no se encuentra en la region')
                return redirect('Add_paises')
            Crear_Pais(nombre_pais, region_pais, continente_pais, nacionalidad, descripcion_pais)
            
            return redirect ('Show_paises')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_paises')
    form = Form_Paises()
    return render(request, 'create_edit/AddPaises.html',{'form':form})

def Add_Rallies(request):
    if request.method == 'POST':
        form = Form_Rallies(request.POST)
        try:
            del form.errors['duracion']    
        except:
            pass
        if form.is_valid():
            nombre_rally = form.data['nombre_rally'] 
            costo_participante = form.data['costo_participante'] 
            f_inicio = form.data['f_inicio'] 
            f_fin = form.data['f_fin'] 
            tipo_rally = form.data['tipo_rally'] 
            total_cupo_participante = form.data['total_cupo_participante'] 
            # DEBERIA DE EXISTIR UNA RESTRICCION DE QUE SOLO PUEDE HABER 3 RALLIES AL AÑO
            if form.cleaned_data.get('f_fin') > form.cleaned_data.get('f_inicio') + timedelta(days=7):
                messages.error(request, 'Los Rally deben tener maximo una semana de duración')
                return redirect('Add_rallies')
            if form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio'):
                messages.error(request, 'La fecha fin no es la adecuanda')
                return redirect('Add_rallies')
            ff = form.cleaned_data.get('f_fin')
            fi = form.cleaned_data.get('f_inicio')
            duracion = 1
            while ff > fi:
                duracion = duracion+1
                fi = fi + timedelta(days=1)
            Crear_Rally(nombre_rally, costo_participante, f_inicio, f_fin, tipo_rally, duracion, total_cupo_participante)  
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
            id_pais = form.data['id_pais']  
            nombre_ciudad= form.data['nombre_ciudad'] 
            tipo_ciudad= form.data['tipo_ciudad'] 
            descripcion_ciudad= form.data['descripcion_ciudad'] 

            Crear_Ciudad(id_pais, nombre_ciudad, tipo_ciudad, descripcion_ciudad)
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
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']
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

def Add_Circuitos(request):
    if request.method == 'POST':
        form = Form_Circuitos(request.POST)
        try:
            del form.errors['orden_circuito']    
        except:
            pass
        if form.is_valid():
            orden_circuito = form.data['orden_circuito']  
            id_rally = form.data['id_rally']  
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']
            maxdias = form.data['maxdias']
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Add_Circuitos')

            Crear_Circuito(orden_circuito, id_rally, id_ciudad, id_pais, maxdias)
            return redirect ('Show_Circuitos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Circuitos')
    form = Form_Circuitos()
    return render(request, 'create_edit/AddCircuitos.html',{'form':form})

def Add_ATR_CIR(request):
    if request.method == 'POST':
        form = Form_ATR_CIR(request.POST)
        try:
            del form.errors['id_atraccion']    
        except:
            pass
        if form.is_valid():
            id_atraccion = form.data['id_atraccion']  
            id_ciudad_at = form.data['id_ciudad_at']
            id_pais_at = form.data['id_pais_at']
            id_circuito = form.data['id_circuito']
            id_rally_cir = form.data['id_rally_cir']  
            id_ciudad_cir = form.data['id_ciudad_cir']
            id_pais_cir = form.data['id_pais_cir']
            orden = form.data['orden']

            try:
                atraccion = Atracciones.objects.get(id_ciudad=id_ciudad_at, id_pais=id_pais_at, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Add_atr_cir')

            try:
                circuito = Circuitos.objects.get(orden_circuito=id_circuito, id_rally=id_rally_cir, id_ciudad=id_ciudad_cir, id_pais=id_pais_cir)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'Error, la estructura del circuito viola integridad')
                return redirect('Add_atr_cir')

            Crear_ATR_CIR(id_atraccion, id_ciudad_at, id_pais_at, id_circuito, id_rally_cir, id_ciudad_cir, id_pais_cir, orden)
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

            nombre = form.data['nombre'] 
            tipo_de_operacion = form.data['tipo_de_operacion'] 
            alcance_geografico = form.data['alcance_geografico'] 
            web = form.data['web'] 
            telefono = form.data['telefono'] 
            calle_av = form.data['calle_av'] 
            id_ciudad = form.data['id_ciudad'] 
            id_pais = form.data['id_pais'] 
            descripcion = form.data['descripcion'] 
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Add_Agencia_de_viajes')
            Crear_Agencia(nombre, tipo_de_operacion, alcance_geografico, web, telefono, calle_av, id_ciudad, id_pais, descripcion)
            #form.save()
            return redirect ('Show_Agencia_de_viajes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Agencia_de_viajes')
    form = Form_Agencia_de_viajes()
    return render(request, 'create_edit/AddAgencia_de_viajes.html',{'form':form})

def Add_AGE_AGE(request):
    if request.method == 'POST':
        form = Form_AGE_AGE(request.POST)
        try:
            del form.errors['id_agencia']    
        except:
            pass
        if form.is_valid():

            id_agencia = form.data['id_agencia']  
            id_socio = form.data['id_socio']
            f_inicio = form.data['f_inicio']
            f_fin = form.data['f_fin']
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
            
            if (form.cleaned_data.get('f_fin')!=None) and (form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio')):
                messages.error(request, 'Fecha Fin debe ser mayor a fecha inicio')
                return redirect('Add_AGE_AGE')

            Crear_AGE_AGE(id_agencia, id_socio, f_inicio, f_fin)
            return redirect ('Show_AGE_AGE')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_AGE_AGE')
    form = Form_AGE_AGE()
    return render(request, 'create_edit/AddAGE_AGE.html',{'form':form})

def Add_Cupos(request):
    if request.method == 'POST':
        form = Form_Cupos(request.POST)
        try:
            del form.errors['id_agencia']    
        except:
            pass
        if form.is_valid():
            id_agencia = form.data['id_agencia']  
            id_rally = form.data['id_rally']
            cantidad = form.data['cantidad']
            try:
                validacion = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'No existe la agencia')
                return redirect('Add_Cupos')
            Crear_Cupo(id_agencia, id_rally, cantidad)
            return redirect ('Show_Cupos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Cupos')
    form = Form_Cupos()
    return render(request, 'create_edit/AddCupos.html',{'form':form})
        
def Add_Registro_clientes(request): 
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
            
            try:
                validacion = Clientes.objects.get(doc_identidad_o_rif=id_cliente)
            except Clientes.DoesNotExist:        
                messages.error(request, 'No existe el cliente')
                return redirect('Add_Registro_clientes')
            Crear_Registro_clientes(id_cliente, id_agencia, f_registro, 1)
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
            nombre = form.cleaned_data.get('nombre')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Add_Alojamientos')
            Crear_Alojamiento(id_ciudad, id_pais, nombre)
            #form.save()
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
            id_alojamiento = form.data['id_alojamiento']  
            nombre_proveedor = form.cleaned_data.get('nombre_proveedor')
            tipo_proveedor = form.cleaned_data.get('tipo_proveedor')
            Crear_Proveedor(id_alojamiento, nombre_proveedor, tipo_proveedor)
            #form.save()
            return redirect ('Show_Proveedores')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Proveedores')
    form = Form_Proveedores()
    return render(request, 'create_edit/AddProveedores.html',{'form':form})

def Add_PRO_AGE(request):
    if request.method == 'POST':
        form = Form_PRO_AGE(request.POST)
        try:
            del form.errors['id_agencia']    
        except:
            pass
        if form.is_valid():

            id_agencia = form.data['id_agencia']  
            id_proveedor = form.data['id_proveedor']
            f_inicio = form.data['f_inicio']
            f_fin = form.data['f_fin']
            try:
                validacion = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'No existe la agencia')
                return redirect('Add_pro_age')
            if (form.cleaned_data.get('f_fin')!=None) and (form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio')):
                messages.error(request, 'Fecha Fin debe ser mayor a fecha inicio')
                return redirect('Add_pro_age')
                
            val = Proveedores.objects.get(id_proveedor=id_proveedor)
            if val.tipo_proveedor == 'exclusivo':
                try:
                    val = PRO_AGE.objects.get(id_proveedor=id_proveedor)
                except PRO_AGE.DoesNotExist:        
                    Crear_PRO_AGE(id_agencia, id_proveedor, f_inicio, f_fin)
                    return redirect ('Show_pro_age')
                messages.error(request, 'Este proveedor es exclusivo de otra agencia')
                return redirect('Add_pro_age')

            Crear_PRO_AGE(id_agencia, id_proveedor, f_inicio, f_fin)
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
            primer_nombre = form.data['primer_nombre']  
            primer_apellido = form.data['primer_apellido']
            segundo_apellido = form.data['segundo_apellido']
            telefono = form.data['telefono']
            segundo_nombre = form.data['segundo_nombre']
            Crear_Asesor_viaje(primer_nombre, primer_apellido, segundo_apellido, telefono, segundo_nombre)
            #form.save()
            return redirect ('Show_Asesores_de_viajes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Asesores_de_viajes')
    form = Form_Asesores_de_viajes()
    return render(request, 'create_edit/AddAsesores_de_viajes.html',{'form':form})

def Add_Paquetes(request):
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

def Add_Especializaciones(request):
    if request.method == 'POST':
        form = Form_Especializaciones(request.POST)
        if form.is_valid():
            id_atraccion = form.data['id_atraccion']
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']  
            id_paquete = form.data['id_paquete']  
            id_agencia_paquete = form.data['id_agencia_paquete']

            try:
                validacion = Atracciones.objects.get(id_ciudad=id_ciudad, id_pais=id_pais, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Add_Especializaciones')
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

def Add_Precios_paquetes(request): 
    if request.method == 'POST':
        form = Form_Precios_paquetes(request.POST)
        try:
            del form.errors['f_inicio']    
        except:
            pass
        if form.is_valid():

            f_inicio = form.data['f_inicio']  
            id_paquete = form.data['id_paquete']
            id_agencia = form.data['id_agencia']
            f_fin = form.data['f_fin']
            valor = form.data['valor']
            if (form.cleaned_data.get('f_fin')!=None) and (form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio')):
                messages.error(request, 'Fecha Fin debe ser mayor a fecha inicio')
                return redirect('Add_Precios_paquetes')
            try:
                validacion = Paquetes.objects.get(id_paquete=id_paquete, id_agencia=id_agencia)
            except Paquetes.DoesNotExist:        
                messages.error(request, 'Error, el paquete no pertenece a la agencia')
                return redirect('Add_Precios_paquetes')

            try:
                val = Precios_paquetes.objects.filter(id_paquete=id_paquete, id_agencia=id_agencia)
            except Precios_paquetes.DoesNotExist:        
                Crear_Precio_paquete(f_inicio, id_paquete, id_agencia, f_fin, valor)
                return redirect ('Show_Precios_paquetes')

            for o in val:
                if (o.f_inico < form.cleaned_data.get('f_fin')):
                    messages.error(request, 'Error, En ese rango de fechas ya existe un paquete activo')
                    return redirect('Add_Precios_paquetes')
                if (o.f_fin==None) or (o.f_fin > form.cleaned_data.get('f_inicio') or (o.f_inico < form.cleaned_data.get('f_fin'))):
                    messages.error(request, 'Error, En ese rango de fechas ya existe un paquete activo')
                    return redirect('Add_Precios_paquetes')

            #return HttpResponse(True)

            Crear_Precio_paquete(f_inicio, id_paquete, id_agencia, f_fin, valor)
            return redirect ('Show_Precios_paquetes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Precios_paquetes')
    form = Form_Precios_paquetes()
    return render(request, 'create_edit/AddPrecios_paquetes.html',{'form':form})

def Add_Calendarios_anuales(request):
    if request.method == 'POST':
        form = Form_Calendarios_anuales(request.POST)
        try:
            del form.errors['f_salida']    
        except:
            pass
        if form.is_valid():
            f_salida = form.data['f_salida']  
            id_paquete = form.data['id_paquete']
            id_agencia = form.data['id_agencia']
            descripcion = form.data['descripcion']
            Crear_Calendarios_anuales(f_salida, id_paquete, id_agencia, descripcion)
            return redirect ('Show_Calendarios_anuales')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Calendarios_anuales')
    form = Form_Calendarios_anuales()
    return render(request, 'create_edit/AddCalendarios_anuales.html',{'form':form})

def Add_Descuentos(request):
    if request.method == 'POST':
        form = Form_Descuentos(request.POST)
        if form.is_valid():
            if (form.cleaned_data.get('f_fin')!=None) and (form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio')):
                messages.error(request, 'Fecha Fin debe ser mayor a fecha inicio')
                return redirect('Add_Descuentos')
            if form.cleaned_data.get('cant_per_gratis')!=None and form.cleaned_data.get('tipo_descuento')!= 'viajerosgratis':
                messages.error(request, 'No puedes agregar personas gratis a ese tipo de descuento')
                return redirect('Add_Descuentos')
            if form.cleaned_data.get('porcentaje')==None and form.cleaned_data.get('tipo_descuento')!= 'viajerosgratis':
                messages.error(request, 'Falta agregar porcentaje de descuento')
                return redirect('Add_Descuentos')
            form.save()
            return redirect ('Show_Descuentos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Descuentos')
    form = Form_Descuentos()
    return render(request, 'create_edit/AddDescuentos.html',{'form':form})

def Add_Intinerarios(request):
    if request.method == 'POST':
        form = Form_Itinerarios(request.POST)
        try:
            del form.errors['orden']    
        except:
            pass
        if form.is_valid():
            orden = form.data['orden']  
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']
            id_agencia = form.data['id_agencia']
            id_paquete = form.data['id_paquete']  
            tiempo_estadia = form.data['tiempo_estadia']
            try:
                validacion = Paquetes.objects.get(id_paquete=id_paquete, id_agencia=id_agencia)
            except Paquetes.DoesNotExist:        
                messages.error(request, 'Error, el paquete no pertenece a la agencia')
                return redirect('Add_Intinerarios')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Add_Intinerarios')

            Crear_Itinerarios(orden, id_ciudad, id_pais, id_agencia, id_paquete, tiempo_estadia)
            return redirect ('Show_Intinerarios')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Intinerarios')
    form = Form_Itinerarios()
    return render(request, 'create_edit/AddIntinerarios.html',{'form':form})

def Add_ITN_ATR(request):
    if request.method == 'POST':
        form = Form_ITN_ATR(request.POST)
        try:
            del form.errors['id_itinerario']    
        except:
            pass
        if form.is_valid():
            id_itinerario = form.data['id_itinerario']  
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']
            id_agencia = form.data['id_agencia']
            id_paquete = form.data['id_paquete']  
            id_atraccion = form.data['id_atraccion']
            id_ciudad_at = form.data['id_ciudad_at']
            id_pais_at = form.data['id_pais_at']
            orden_visita = form.data['orden_visita']
            try:
                validacion = Atracciones.objects.get(id_ciudad=id_ciudad, id_pais=id_pais, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Add_ITN_ATR')
            try:
                validacion = Itinerarios.objects.get(orden=id_itinerario, id_ciudad=id_ciudad, id_pais=id_pais, id_agencia=id_agencia, id_paquete=id_paquete)
            except Itinerarios.DoesNotExist:        
                messages.error(request, 'Error con la union de itinerario, ciudad, pais, agencia, paquete')
                return redirect('Add_ITN_ATR') 

            Crear_ITN_ATR(id_itinerario, id_ciudad, id_pais, id_agencia, id_paquete, id_atraccion, id_ciudad_at, id_pais_at, orden_visita)
            return redirect ('Show_ITN_ATR')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_ITN_ATR')
    form = Form_ITN_ATR()
    return render(request, 'create_edit/AddITN_ATR.html',{'form':form})

def Add_Detalles_servicios(request):
    if request.method == 'POST':
        form = Form_Detalles_servicios(request.POST)
        if form.is_valid(): 
            id_itinerario = form.data['id_itinerario']
            id_paquete = form.data['id_paquete']
            id_agencia = form.data['id_agencia']
            id_ciudad = form.data['id_ciudad']  
            id_pais = form.data['id_pais']
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

def Add_ALO_DET(request):
    if request.method == 'POST':
        form = Form_ALO_DET(request.POST)
        try:
            del form.errors['id_detalle_servicio']    
        except:
            pass
        if form.is_valid():

            id_detalle_servicio = form.data['id_detalle_servicio']  
            id_itinerario = form.data['id_itinerario']
            id_paquete = form.data['id_paquete']
            id_agencia = form.data['id_agencia']  
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']
            id_alojamiento = form.data['id_alojamiento']
            try:
                validacion = Detalles_servicios.objects.get(id_detalle_servicio=id_detalle_servicio, id_itinerario=id_itinerario, id_ciudad=id_ciudad, id_pais=id_pais, id_agencia=id_agencia, id_paquete=id_paquete)
            except Detalles_servicios.DoesNotExist:        
                messages.error(request, 'Error con la union de itinerario, ciudad, pais, agencia, paquete y detalle servicio')
                return redirect('Add_ALO_DET')

            Crear_ALO_DET(id_detalle_servicio, id_itinerario, id_paquete, id_agencia, id_ciudad, id_pais, id_alojamiento)
            return redirect ('Show_ALO_DET')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_ALO_DET')
    form = Form_ALO_DET()
    return render(request, 'create_edit/AddALO_DET.html',{'form':form})

def Add_Instrumentos_de_pago(request):
    if request.method == 'POST':
        form = Form_Instrumentos_de_pago(request.POST)
        if form.is_valid():
            doc_identidad_cliente = form.data['doc_identidad_cliente']
            try:
                validacion = Clientes.objects.get(doc_identidad_o_rif=doc_identidad_cliente)
            except Clientes.DoesNotExist:        
                messages.error(request, 'Cliente no existe')
                return redirect('Add_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') == 'zelle' and form.cleaned_data.get('id_banco')!=None:
                messages.error(request, 'El tipo de instrumento no debe estar vinculado con un banco')
                return redirect('Add_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') == 'zelle' and form.cleaned_data.get('numero_zelle')==None:
                messages.error(request, 'Falto Vincular numero zelle')
                return redirect('Add_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') == 'zelle' and form.cleaned_data.get('email_zelle')==None:
                messages.error(request, 'Falto Vincular Email zelle')
                return redirect('Add_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') != 'zelle' and form.cleaned_data.get('id_banco')==None:
                messages.error(request, 'El tipo de instrumento debe estar vinculado con un banco')
                return redirect('Add_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') != 'zelle' and form.cleaned_data.get('numero_zelle')!=None:
                messages.error(request, 'No se puede vincular numero zelle')
                return redirect('Add_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') != 'zelle' and form.cleaned_data.get('email_zelle')!=None:
                messages.error(request, 'No se puede vincular email zelle')
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

def Add_Formas_de_pago(request):
    if request.method == 'POST':
        form = Form_Formas_de_pago(request.POST)
        if form.is_valid():

            id_instrumento = form.data['id_instrumento']  
            id_cliente = form.data['id_cliente']
            id_paquete_contrato = form.data['id_paquete_contrato']
            tipo_forma_de_pago = form.data['tipo_forma_de_pago']
            try:
                validacion = Instrumentos_de_pago.objects.get(id_instrumento=id_instrumento, doc_identidad_cliente=id_cliente)
            except Instrumentos_de_pago.DoesNotExist:        
                messages.error(request, 'Error, instrumento de pago y cliente no coinciden')
                return redirect('Add_Formas_de_pago')
            try:
                validacion = Paquetes_contrato.objects.get(numero_factura=id_paquete_contrato)
            except Paquetes_contrato.DoesNotExist:        
                messages.error(request, 'Error, paquete contrato invalido')
                return redirect('Add_Formas_de_pago')

            Crear_Forma_de_pago(id_instrumento, id_cliente, id_paquete_contrato, tipo_forma_de_pago)
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

def Add_PAI_VIA(request):
    if request.method == 'POST':
        form = Form_PAI_VIA(request.POST)
        try:
            del form.errors['id_viajero']    
        except:
            pass
        if form.is_valid():
            id_viajero = form.data['id_viajero']  
            id_pais = form.data['id_pais']
            nro_de_pasaporte = form.data['nro_de_pasaporte']
            try:
                validacion = Viajeros.objects.get(id_de_identidad=id_viajero)
            except Viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero invalido')
                return redirect('Add_PAI_VIA')

            Crear_PAI_VIA(id_viajero, id_pais, nro_de_pasaporte)
            return redirect ('Show_PAI_VIA')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_PAI_VIA')
    form = Form_PAI_VIA()
    return render(request, 'create_edit/AddPAI_VIA.html',{'form':form})

def Add_Registro_viajeros(request):
    if request.method == 'POST':
        form = Form_Registro_viajeros(request.POST)
        try:
            del form.errors['id_agencia']    
        except:
            pass
        try:
            del form.errors['nro_registro']    
        except:
            pass
        if form.is_valid():
            id_agencia = form.data['id_agencia']  
            id_viajero = form.data['id_viajero']
            f_registro = form.data['f_registro']
            nro_registro = 1
            try:
                validacion = Viajeros.objects.get(id_de_identidad=id_viajero)
            except Viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero invalido')
                return redirect('Add_Registro_viajeros')
            try:
                validacion = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'Error, Agencia invalida')
                return redirect('Add_Registro_viajeros')

            Crear_Registro_viajeros(id_agencia, id_viajero, f_registro, nro_registro)
            return redirect ('Show_Registro_viajeros')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Registro_viajeros')
    form = Form_Registro_viajeros()
    form.fields['nro_registro'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddRegistro_viajeros.html',{'form':form})

def Add_Detalle_viajeros(request):
    if request.method == 'POST':
        form = Form_Detalle_viajeros(request.POST)
        try:
            del form.errors['id_viajero']    
        except:
            pass
        if form.is_valid():
            id_viajero = form.data['id_viajero']
            id_agencia = form.data['id_agencia']
            id_paquete_contrato = form.data['id_paquete_contrato']
            try:
                validacion = Registro_viajeros.objects.get(id_agencia=id_agencia, id_viajero=id_viajero)
            except Registro_viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero no pertenece a la agencia')
                return redirect('Add_Detalle_viajeros')
            try:
                validacion = Paquetes_contrato.objects.get(numero_factura=id_paquete_contrato)
            except Paquetes_contrato.DoesNotExist:        
                messages.error(request, 'Error, Paquete invalido')
                return redirect('Add_Detalle_viajeros')

            Crear_Detalle_viajero(id_viajero, id_agencia, id_paquete_contrato)
            return redirect ('Show_Detalle_viajeros')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Add_Detalle_viajeros')
    form = Form_Detalle_viajeros()
    return render(request, 'create_edit/AddDetalle_viajeros.html',{'form':form})

def Add_Participantes(request):
    if request.method == 'POST':
        form = Form_Participantes(request.POST)
        if form.is_valid():
            id_via_agencia = form.data['id_via_agencia']
            id_via_viajero = form.data['id_via_viajero']
            id_cli_cliente = form.data['id_cli_cliente']  
            id_cli_agencia = form.data['id_cli_agencia']

            try:
                validacion = Registro_viajeros.objects.get(id_agencia=id_via_agencia, id_viajero=id_via_viajero)
            except Registro_viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero no pertenece a la agencia')
                return redirect('Add_Participantes')
            try:
                validacion = Registro_clientes.objects.get(id_cliente=id_cli_cliente, id_agencia=id_cli_agencia)
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

#DELETE -------------------------------------------------------------------------------------------------------------------------------------

def Delete_Bancos(request, id):
    try:
        obj = Bancos.objects.get(pk=id)
    except Bancos.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_bancos')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_bancos')
    return redirect('Show_bancos')

def Delete_Clientes(request, id):
    try:
        obj = Clientes.objects.get(pk=id)
    except Clientes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Clientes')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Clientes')
    return redirect('Show_Clientes')

def Delete_Areas_de_interes(request, id):
    try:
        obj = Areas_de_interes.objects.get(pk=id)
    except Areas_de_interes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Areas_de_interes')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Areas_de_interes')
    return redirect('Show_Areas_de_interes')

def Delete_Paises(request, id):
    try:
        obj = Paises.objects.get(pk=id)
    except Paises.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_paises')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_paises')
    return redirect('Show_paises')

def Delete_Rallies(request, id):
    try:
        obj = Rallies.objects.get(pk=id)
    except Rallies.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_rallies')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_rallies')
    return redirect('Show_rallies')

def Delete_Premios(request, id, id2):
    try:
        rallie = Rallies.objects.get(nombre_rally=id2)
    except Rallies.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_premios')
    try:
        obj = Premios.objects.filter(id_rally=rallie.id_rally).get(id_premio=id)
    except Premios.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_premios')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_premios')
    return redirect('Show_premios')

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
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Ciudades')
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
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Atracciones')
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
    if Borrar_Circuito(id, rallie.id_rally, ciudad.id_ciudad, pais.id_pais) == 1:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Circuitos')
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
        obj = ATR_CIR.objects.filter(id_ciudad_at=ciudad_at.id_ciudad,id_pais_at=pais_at.id_pais,id_circuito=circuito.orden_circuito,id_rally_cir=rallie.id_rally,id_ciudad_cir=ciudad_cir.id_ciudad,id_pais_cir=pais_cir.id_pais).get(id_atraccion=id)
    except ATR_CIR.DoesNotExist:        
        messages.error(request, 'No existe la entrada8')
        return redirect('Show_atr_cir')
    try:
        Borrar_ATR_CIR(atraccion.id_atraccion, ciudad_at.id_ciudad, pais_at.id_pais, circuito.orden_circuito, rallie.id_rally, ciudad_cir.id_ciudad, pais_cir.id_pais)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_atr_cir')
    
    return redirect('Show_atr_cir')

def Delete_Agencia_de_viajes(request, id):
    try:
        obj = Agencias_de_viajes.objects.get(pk=id)
    except Agencias_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Agencia_de_viajes')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Agencia_de_viajes')
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
    try:
        Borrar_AGE_AGE(id, socio.id_agencia)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_AGE_AGE')
    
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
    try:
        Borrar_Cupo(id, rallie.id_rally)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Cupos')
    
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
    try:
        Borrar_Registro_clientes(id, agencia.id_agencia)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Registro_clientes')
    
    return redirect('Show_Registro_clientes')

def Delete_Alojamientos(request, id):
    try:
        obj = Alojamientos.objects.get(pk=id)
    except Alojamientos.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Alojamientos')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Alojamientos')
    return redirect('Show_Alojamientos')

def Delete_Proveedores(request, id):
    try:
        obj = Proveedores.objects.get(pk=id)
    except Proveedores.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Proveedores')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Proveedores')
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
    try:
        Borrar_PRO_AGE(id, proveedor.id_proveedor)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_pro_age')
    
    return redirect('Show_pro_age')

def Delete_Asesores_de_viajes(request, id):
    try:
        obj = Asesores_de_viajes.objects.get(pk=id)
    except Asesores_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Asesores_de_viajes')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Asesores_de_viajes')
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
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Paquetes')
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
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Especializaciones')
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
    try:
        Borrar_Precio_paquete(id,paquete.id_paquete, agencia.id_agencia)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Precios_paquetes')
    
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
    try:
        Borrar_Calendarios_anuales(id, paquete.id_paquete, agencia.id_agencia)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Calendarios_anuales')

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
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Descuentos')
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
    try:
        Borrar_Itinerarios(id, ciudad.id_ciudad, pais.id_pais, agencia.id_agencia, paquete.id_paquete)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Intinerarios')
    
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
    if Borrar_ITN_ATR(id, ciudad.id_ciudad, pais.id_pais, agencia.id_agencia, paquete.id_paquete, atraccion.id_atraccion, ciudad_at.id_ciudad, pais_at.id_pais) == 1:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_ITN_ATR')
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
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Detalles_servicios')
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
    if Borrar_ALO_DET(id, itinerario.orden, paquete.id_paquete, agencia.id_agencia, ciudad.id_ciudad, pais.id_pais, alojamiento.id_alojamiento) == 1:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_ALO_DET')
    
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
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Instrumentos_de_pago')
    return redirect('Show_Instrumentos_de_pago')

def Delete_Paquetes_contrato(request, id):
    try:
        obj = Paquetes_contrato.objects.get(pk=id)
    except Paquetes_contrato.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Paquetes_contrato')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Paquetes_contrato')
    return redirect('Show_Paquetes_contrato')

def Delete_Formas_de_pago(request, id):
    try:
        Borrar_Forma_de_pago(id)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Formas_de_pago')
    
    return redirect('Show_Formas_de_pago')

def Delete_Viajeros(request, id):
    try:
        obj =Viajeros.objects.get(pk=id)
    except Viajeros.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Viajeros')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Viajeros')
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
    try:
        Borrar_PAI_VIA(id, pais.id_pais)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_PAI_VIA')
    
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
    if Borrar_Registro_viajeros(agencia.id_agencia, viajero.id_de_identidad) == 1:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Registro_viajeros')
    
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
    try:
        Borrar_Detalle_viajero(id, agencia.id_agencia, paq_cont.numero_factura)
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Detalle_viajeros')
    
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
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Participantes')
    return redirect('Show_Participantes')

def Delete_Puntuaciones(request, id):
    try:
        obj = Puntuaciones.objects.get(id_puntuacion=id)
    except Puntuaciones.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Puntuaciones')
    try:
        obj.delete()
    except ProtectedError:
        messages.error(request, 'Existen registros vinculados')
        return redirect('Show_Puntuaciones')
    return redirect('Show_Puntuaciones')

#EDIT --------------------------------------------------------------------------------------------------------------------------------------

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
            return redirect('Show_bancos')
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
            return redirect('Show_Clientes')
    form = Form_Clientes(instance= obj)
    form.fields['doc_identidad_o_rif'].widget.attrs['readonly'] = True
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
            return redirect('Show_Areas_de_interes')
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
            region_pais = form.data['region_pais']  
            continente_pais = form.data['continente_pais'] 
            if region_pais == "EU" and continente_pais == "Europa":
                pass
            elif region_pais == "AF_MO" and continente_pais == "Africa":
                pass
            elif region_pais == "AF_MO" and continente_pais == "Asia":
                pass
            elif region_pais == "AU_NZ_PAC" and continente_pais == "Oceania":
                pass
            elif region_pais == "AS" and continente_pais == "Asia":
                pass
            elif region_pais == "MEX_CEN_SUR" and continente_pais == "America":
                pass
            elif region_pais == "USA_CAN_CAR" and continente_pais == "America":
                pass
            else:
                messages.error(request, 'El continento no se encuentra en la region')
                return redirect('Show_paises')
            form.save()
            return redirect ('Show_paises')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_paises')
    form = Form_Paises(instance= obj)
    return render(request, 'create_edit/AddPaises.html',{'form':form})

def Edit_Rallies(request, id):
    try:
        obj = Rallies.objects.get(id_rally=id)                   #---> cambiar id
    except Rallies.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('Show_rallies')                         #---> cambiar show
    if request.method == 'POST':
        form = Form_Rallies(request.POST, instance= obj)        #---> poner instance
        try:
            del form.errors['duracion']    
        except:
            pass
        if form.is_valid():
            nombre_rally = form.data['nombre_rally'] 
            costo_participante = form.data['costo_participante'] 
            f_inicio = form.data['f_inicio'] 
            f_fin = form.data['f_fin'] 
            tipo_rally = form.data['tipo_rally'] 
            total_cupo_participante = form.data['total_cupo_participante'] 
            id_rally = id
            # DEBERIA DE EXISTIR UNA RESTRICCION DE QUE SOLO PUEDE HABER 3 RALLIES AL AÑO
            if form.cleaned_data.get('f_fin') > form.cleaned_data.get('f_inicio') + timedelta(days=7):
                messages.error(request, 'Los Rally deben tener maximo una semana de duración')
                return redirect('Show_rallies')
            if form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio'):
                messages.error(request, 'La fecha fin no es la adecuanda')
                return redirect('Show_rallies')
            ff = form.cleaned_data.get('f_fin')
            fi = form.cleaned_data.get('f_inicio')
            duracion = 1
            while ff > fi:
                duracion = duracion+1
                fi = fi + timedelta(days=1)

            act_Rally(nombre_rally, costo_participante, f_inicio, f_fin, tipo_rally, duracion, total_cupo_participante, id_rally)
        
            return redirect ('Show_rallies')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_rallies')
    form = Form_Rallies(instance= obj)                          #---> cambiar intance
    return render(request, 'create_edit/AddRallies.html',{'form':form})

def Edit_Premios(request, id, id2): 
    try:
        rallie = Rallies.objects.get(nombre_rally=id2)
    except Rallies.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_premios')
    try:
        obj = Premios.objects.filter(id_rally=rallie.id_rally).get(id_premio=id)  
    except Premios.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('Show_premios')      
    if request.method == 'POST':
        form = Form_Premios(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect ('Show_premios')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_premios')
    form = Form_Premios(instance= obj)
    form.fields['id_rally'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddPremios.html',{'form':form})

def Edit_Ciudades(request, id, id2):
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
    if request.method == 'POST':
        form = Form_Ciudades(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect ('Show_Ciudades')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Ciudades')
    form = Form_Ciudades(instance= obj)
    form.fields['id_pais'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddCiudades.html',{'form':form})

def Edit_Atracciones(request, id, id2, id3):
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
    if request.method == 'POST':
        form = Form_Atracciones(request.POST, instance= obj)

        if form.is_valid():
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Show_Atracciones')
            form.save()
            return redirect ('Show_Atracciones')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Atracciones')
    form = Form_Atracciones(instance= obj)
    form.fields['id_ciudad'].widget.attrs['readonly'] = True 
    form.fields['id_pais'].widget.attrs['readonly'] = True 
    return render(request, 'create_edit/AddAtracciones.html',{'form':form})
    
def Edit_Circuitos(request, id,id2,id3,id4):
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
    if request.method == 'POST':
        form = Form_Circuitos(request.POST, instance= obj)
        try:
            del form.errors['orden_circuito']    
        except:
            pass
        if form.is_valid():
            orden_circuito = form.data['orden_circuito']  
            id_rally = form.data['id_rally']  
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']
            maxdias = form.data['maxdias']
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Show_Circuitos')

            Actualizar_Circuito(orden_circuito, id_rally, id_ciudad, id_pais, maxdias)
            return redirect ('Show_Circuitos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Circuitos')
    form = Form_Circuitos(instance= obj)
    form.fields['orden_circuito'].widget.attrs['readonly'] = True
    form.fields['id_rally'].widget.attrs['readonly'] = True
    form.fields['id_ciudad'].widget.attrs['readonly'] = True
    form.fields['id_pais'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddCircuitos.html',{'form':form})

def Edit_ATR_CIR(request, id,id2,id3,id4,id5,id6,id7):
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
        obj = ATR_CIR.objects.filter(id_ciudad_at=ciudad_at.id_ciudad,id_pais_at=pais_at.id_pais,id_circuito=circuito.orden_circuito,id_rally_cir=rallie.id_rally,id_ciudad_cir=ciudad_cir.id_ciudad,id_pais_cir=pais_cir.id_pais).get(id_atraccion=id)
    except ATR_CIR.DoesNotExist:        
        messages.error(request, 'No existe la entrada8')
        return redirect('Show_atr_cir')
    if request.method == 'POST':
        form = Form_ATR_CIR(request.POST, instance= obj)
        try:
            del form.errors['id_atraccion']    
        except:
            pass
        if form.is_valid():
            id_atraccion = form.data['id_atraccion']  
            id_ciudad_at = form.data['id_ciudad_at']
            id_pais_at = form.data['id_pais_at']
            id_circuito = form.data['id_circuito']
            id_rally_cir = form.data['id_rally_cir']  
            id_ciudad_cir = form.data['id_ciudad_cir']
            id_pais_cir = form.data['id_pais_cir']
            orden = form.data['orden']

            try:
                atraccion = Atracciones.objects.get(id_ciudad=id_ciudad_at, id_pais=id_pais_at, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Show_atr_cir')

            try:
                circuito = Circuitos.objects.get(orden_circuito=id_circuito, id_rally=id_rally_cir, id_ciudad=id_ciudad_cir, id_pais=id_pais_cir)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'Error, la estructura del circuito viola integridad')
                return redirect('Show_atr_cir')

            Actualizar_ATR_CIR(id_atraccion, id_ciudad_at, id_pais_at, id_circuito, id_rally_cir, id_ciudad_cir, id_pais_cir, orden)
            return redirect ('Show_atr_cir')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_atr_cir')
    form = Form_ATR_CIR(instance= obj)
    form.fields['id_atraccion'].widget.attrs['readonly'] = True
    form.fields['id_ciudad_at'].widget.attrs['readonly'] = True
    form.fields['id_pais_at'].widget.attrs['readonly'] = True
    form.fields['id_circuito'].widget.attrs['readonly'] = True
    form.fields['id_rally_cir'].widget.attrs['readonly'] = True
    form.fields['id_ciudad_cir'].widget.attrs['readonly'] = True
    form.fields['id_pais_cir'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddATR_CIR.html',{'form':form})

def Edit_Agencia_de_viajes(request, id):
    try:
        obj = Agencias_de_viajes.objects.get(pk=id)
    except Agencias_de_viajes.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Agencia_de_viajes')
    if request.method == 'POST':
        form = Form_Agencia_de_viajes(request.POST, instance= obj)
        if form.is_valid():

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Show_Agencia_de_viajes')

            form.save()
            return redirect ('Show_Agencia_de_viajes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Agencia_de_viajes')
    form = Form_Agencia_de_viajes(instance= obj)
    return render(request, 'create_edit/AddAgencia_de_viajes.html',{'form':form})

def Edit_AGE_AGE(request, id,id2):
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
    if request.method == 'POST':
        form = Form_AGE_AGE(request.POST, instance= obj)
        try:
            del form.errors['id_agencia']    
        except:
            pass
        if form.is_valid():

            id_agencia = form.data['id_agencia']  
            id_socio = form.data['id_socio']
            f_inicio = form.data['f_inicio']
            f_fin = form.data['f_fin']
            try:
                ciudad = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'No existe la agencia')
                return redirect('Show_AGE_AGE')
            try:
                ciudad = Agencias_de_viajes.objects.get(id_agencia=id_socio)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'No existe el socio')
                return redirect('Show_AGE_AGE')
            if (form.cleaned_data.get('f_fin')!=None) and (form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio')):
                messages.error(request, 'Fecha Fin debe ser mayor a fecha inicio')
                return redirect('Show_AGE_AGE')
            Actualizar_AGE_AGE(id_agencia, id_socio, f_inicio, f_fin)
            return redirect ('Show_AGE_AGE')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_AGE_AGE')
    form = Form_AGE_AGE(instance= obj)
    form.fields['id_socio'].widget.attrs['readonly'] = True
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddAGE_AGE.html',{'form':form})

def Edit_Cupos(request, id,id2):
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
    if request.method == 'POST':
        form = Form_Cupos(request.POST, instance= obj)
        try:
            del form.errors['id_agencia']    
        except:
            pass
        if form.is_valid():
            id_agencia = form.data['id_agencia']  
            id_rally = form.data['id_rally']
            cantidad = form.data['cantidad']
            try:
                validacion = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'No existe la agencia')
                return redirect('Show_Cupos')
            Actualizar_Cupo(id_agencia, id_rally, cantidad)
            return redirect ('Show_Cupos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Cupos')
    form = Form_Cupos(instance= obj)
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    form.fields['id_rally'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddCupos.html',{'form':form})

def Edit_Registro_clientes(request, id,id2):
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
    if request.method == 'POST':
        form = Form_Registro_clientes(request.POST, instance= obj)
        try:
            del form.errors['id_cliente']
        except:
            pass
        if form.is_valid():
            id_cliente = form.data['id_cliente']
            id_agencia = form.data['id_agencia']
            f_registro = form.data['f_registro']
            
            try:
                validacion = Clientes.objects.get(doc_identidad_o_rif=id_cliente)
            except Clientes.DoesNotExist:        
                messages.error(request, 'No existe el cliente')
                return redirect('Show_Registro_clientes')
            Actualizar_Registro_clientes(id_cliente, id_agencia, f_registro, 1)
            #form.save()
            return redirect ('Show_Registro_clientes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Registro_clientes')
    form = Form_Registro_clientes(instance= obj)
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    form.fields['id_cliente'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddRegistro_clientes.html',{'form':form})

def Edit_Alojamientos(request, id):
    try:
        obj = Alojamientos.objects.get(pk=id)
    except Alojamientos.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Agencia_de_viajes')
    if request.method == 'POST':
        form = Form_Alojamientos(request.POST, instance= obj)
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
            return redirect('Show_Alojamientos')
    form = Form_Alojamientos(instance= obj)
    return render(request, 'create_edit/AddAlojamientos.html',{'form':form})

def Edit_Proveedores(request, id):
    try:
        obj = Proveedores.objects.get(pk=id)
    except Bancos.DoesNotExist:
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Proveedores')
    if request.method == 'POST':
        form = Form_Proveedores(request.POST, instance= obj)
        if form.is_valid():

            
            if form.data['tipo_proveedor'] == 'exclusivo':
                obj = PRO_AGE.objects.filter(id_proveedor=id)
                f = 0
                for o in obj:
                    f=f+1
                if f>=2:
                    messages.error(request, 'Existen varias agencias asociadas a este proveedor')
                    return redirect('Show_Proveedores')

            form.save()
            return redirect ('Show_Proveedores')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Proveedores')
    form = Form_Proveedores(instance= obj)
    return render(request, 'create_edit/AddProveedores.html',{'form':form})

def Edit_PRO_AGE(request, id,id2):
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
    if request.method == 'POST':
        form = Form_PRO_AGE(request.POST, instance= obj)
        try:
            del form.errors['id_agencia']    
        except:
            pass
        if form.is_valid():
            id_agencia = form.data['id_agencia']  
            id_proveedor = form.data['id_proveedor']
            f_inicio = form.data['f_inicio']
            f_fin = form.data['f_fin']
            if (form.cleaned_data.get('f_fin')!=None) and (form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio')):
                messages.error(request, 'Fecha Fin debe ser mayor a fecha inicio')
                return redirect('Show_pro_age')
            try:
                validacion = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'No existe la agencia')
                return redirect('Show_pro_age')
            
            Actualizar_PRO_AGE(id_agencia, id_proveedor, f_inicio, f_fin)
            return redirect ('Show_pro_age')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_pro_age')
    form = Form_PRO_AGE(instance= obj)
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    form.fields['id_proveedor'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddPRO_AGE.html',{'form':form})

def Edit_Asesores_de_viajes(request, id):
    try:
        obj = Asesores_de_viajes.objects.get(pk=id)
    except Asesores_de_viajes.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Asesores_de_viajes')
    if request.method == 'POST':
        form = Form_Asesores_de_viajes(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect ('Show_Asesores_de_viajes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Asesores_de_viajes')
    form = Form_Asesores_de_viajes(instance= obj)
    return render(request, 'create_edit/AddAsesores_de_viajes.html',{'form':form})

def Edit_Paquetes(request, id,id2):
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
    if request.method == 'POST':
        form = Form_Paquetes(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect ('Show_Paquetes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Paquetes')
    form = Form_Paquetes(instance= obj)
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    form.fields['nombre_paquete'].widget.attrs['readonly'] = True
    form.fields['duracion_dias'].widget.attrs['readonly'] = True
    form.fields['descripcion_turistica'].widget.attrs['readonly'] = True
    form.fields['numero_personas'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddPaquetes.html',{'form':form})

def Edit_Especializaciones(request, id,id2):
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
    if request.method == 'POST':
        form = Form_Especializaciones(request.POST, instance= obj)
        if form.is_valid():
            id_atraccion = form.data['id_atraccion']
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']  
            id_paquete = form.data['id_paquete']  
            id_agencia_paquete = form.data['id_agencia_paquete']

            try:
                validacion = Atracciones.objects.get(id_ciudad=id_ciudad, id_pais=id_pais, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Show_Especializaciones')
            try:
                validacion = Paquetes.objects.get(id_paquete=id_paquete, id_agencia=id_agencia_paquete)
            except Paquetes.DoesNotExist:        
                messages.error(request, 'Error, el paquete no pertenece a la agencia')
                return redirect('Show_Especializaciones')
            form.save()
            return redirect ('Show_Especializaciones')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Especializaciones')
    form = Form_Especializaciones(instance= obj)
    form.fields['id_areas_de_interes'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddEspecializaciones.html',{'form':form})

def Edit_Precios_paquetes(request, id,id2,id3):
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
    if request.method == 'POST':
        form = Form_Precios_paquetes(request.POST, instance= obj)
        try:
            del form.errors['f_inicio']    
        except:
            pass
        if form.is_valid():

            f_inicio = form.data['f_inicio']  
            id_paquete = form.data['id_paquete']
            id_agencia = form.data['id_agencia']
            f_fin = form.data['f_fin']
            valor = form.data['valor']
            if (form.cleaned_data.get('f_fin')!=None) and (form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio')):
                messages.error(request, 'Fecha Fin debe ser mayor a fecha inicio')
                return redirect('Add_Precios_paquetes')
            try:
                validacion = Paquetes.objects.get(id_paquete=id_paquete, id_agencia=id_agencia)
            except Paquetes.DoesNotExist:        
                messages.error(request, 'Error, el paquete no pertenece a la agencia')
                return redirect('Show_Precios_paquetes')

            try:
                val = Precios_paquetes.objects.filter(id_paquete=id_paquete, id_agencia=id_agencia)
            except Precios_paquetes.DoesNotExist:        
                Crear_Precio_paquete(f_inicio, id_paquete, id_agencia, f_fin, valor)
                return redirect ('Show_Precios_paquetes')

            for o in val:
                if (o.f_fin==None) or (o.f_fin > form.cleaned_data.get('f_inicio')):
                    messages.error(request, 'Error, En ese rango de fechas ya existe un paquete activo')
                    return redirect('Add_Precios_paquetes')
                if (o.f_inico < form.cleaned_data.get('f_fin')):
                    messages.error(request, 'Error, En ese rango de fechas ya existe un paquete activo')
                    return redirect('Add_Precios_paquetes')

            Actualizar_Precio_paquete(f_inicio, id_paquete, id_agencia, f_fin, valor)
            return redirect ('Show_Precios_paquetes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Precios_paquetes')
    form = Form_Precios_paquetes(instance= obj)
    form.fields['f_inicio'].widget.attrs['readonly'] = True
    form.fields['id_paquete'].widget.attrs['readonly'] = True
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddPrecios_paquetes.html',{'form':form})

def Edit_Calendarios_anuales(request, id,id2,id3):
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
    if request.method == 'POST':
        form = Form_Calendarios_anuales(request.POST, instance= obj)
        try:
            del form.errors['f_salida']    
        except:
            pass
        if form.is_valid():
            f_salida = form.data['f_salida']  
            id_paquete = form.data['id_paquete']
            id_agencia = form.data['id_agencia']
            descripcion = form.data['descripcion']
            Actualizar_Calendarios_anuales(f_salida, id_paquete, id_agencia, descripcion)
            return redirect ('Show_Calendarios_anuales')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Calendarios_anuales')
    form = Form_Calendarios_anuales(instance= obj)
    form.fields['f_salida'].widget.attrs['readonly'] = True
    form.fields['id_paquete'].widget.attrs['readonly'] = True
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddCalendarios_anuales.html',{'form':form})

def Edit_Descuentos(request, id,id2):
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
    if request.method == 'POST':
        form = Form_Descuentos(request.POST, instance= obj)
        if form.is_valid():
            if (form.cleaned_data.get('f_fin')!=None) and (form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio')):
                messages.error(request, 'Fecha Fin debe ser mayor a fecha inicio')
                return redirect('Show_Descuentos')
            if form.cleaned_data.get('cant_per_gratis')!=None and form.cleaned_data.get('tipo_descuento')!= 'viajerosgratis':
                messages.error(request, 'No puedes agregar personas gratis a ese tipo de descuento')
                return redirect('Show_Descuentos')
            if form.cleaned_data.get('porcentaje')==None and form.cleaned_data.get('tipo_descuento')!= 'viajerosgratis':
                messages.error(request, 'Falta agregar porcentaje de descuento')
                return redirect('Show_Descuentos')
            form.save()
            return redirect ('Show_Descuentos')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Descuentos')
    form = Form_Descuentos(instance= obj)
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddDescuentos.html',{'form':form})

def Edit_Intinerarios(request, id,id2,id3,id4,id5):
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
    if request.method == 'POST':
        form = Form_Itinerarios(request.POST, instance= obj)
        try:
            del form.errors['orden']    
        except:
            pass
        if form.is_valid():
            orden = form.data['orden']  
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']
            id_agencia = form.data['id_agencia']
            id_paquete = form.data['id_paquete']  
            tiempo_estadia = form.data['tiempo_estadia']
            try:
                validacion = Paquetes.objects.get(id_paquete=id_paquete, id_agencia=id_agencia)
            except Paquetes.DoesNotExist:        
                messages.error(request, 'Error, el paquete no pertenece a la agencia')
                return redirect('Show_Intinerarios')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Show_Intinerarios')

            Actualizar_Itinerarios(orden, id_ciudad, id_pais, id_agencia, id_paquete, tiempo_estadia)
            return redirect ('Show_Intinerarios')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Intinerarios')
    form = Form_Itinerarios(instance= obj)
    form.fields['orden'].widget.attrs['readonly'] = True
    form.fields['id_ciudad'].widget.attrs['readonly'] = True
    form.fields['id_pais'].widget.attrs['readonly'] = True
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    form.fields['id_paquete'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddIntinerarios.html',{'form':form})

def Edit_ITN_ATR(request, id,id2,id3,id4,id5,id6,id7,id8):
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
    if request.method == 'POST':
        form = Form_ITN_ATR(request.POST, instance= obj)
        try:
            del form.errors['id_itinerario']    
        except:
            pass
        if form.is_valid():
            id_itinerario = form.data['id_itinerario']  
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']
            id_agencia = form.data['id_agencia']
            id_paquete = form.data['id_paquete']  
            id_atraccion = form.data['id_atraccion']
            id_ciudad_at = form.data['id_ciudad_at']
            id_pais_at = form.data['id_pais_at']
            orden_visita = form.data['orden_visita']
            try:
                validacion = Atracciones.objects.get(id_ciudad=id_ciudad, id_pais=id_pais, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Show_ITN_ATR')
            try:
                validacion = Itinerarios.objects.get(orden=id_itinerario, id_ciudad=id_ciudad, id_pais=id_pais, id_agencia=id_agencia, id_paquete=id_paquete)
            except Itinerarios.DoesNotExist:        
                messages.error(request, 'Error con la union de itinerario, ciudad, pais, agencia, paquete')
                return redirect('Show_ITN_ATR') 

            Actualizar_ITN_ATR(id_itinerario, id_ciudad, id_pais, id_agencia, id_paquete, id_atraccion, id_ciudad_at, id_pais_at, orden_visita)
            return redirect ('Show_ITN_ATR')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_ITN_ATR')
    form = Form_ITN_ATR(instance= obj)
    form.fields['id_itinerario'].widget.attrs['readonly'] = True
    form.fields['id_ciudad'].widget.attrs['readonly'] = True
    form.fields['id_pais'].widget.attrs['readonly'] = True
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    form.fields['id_paquete'].widget.attrs['readonly'] = True
    form.fields['id_atraccion'].widget.attrs['readonly'] = True
    form.fields['id_ciudad_at'].widget.attrs['readonly'] = True
    form.fields['id_pais_at'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddITN_ATR.html',{'form':form})

def Edit_Detalles_servicios(request, id,id2,id3,id4,id5,id6):
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
    if request.method == 'POST':
        form = Form_Detalles_servicios(request.POST, instance= obj)
        if form.is_valid(): 
            id_itinerario = form.data['id_itinerario']
            id_paquete = form.data['id_paquete']
            id_agencia = form.data['id_agencia']
            id_ciudad = form.data['id_ciudad']  
            id_pais = form.data['id_pais']
            try:
                validacion = Itinerarios.objects.get(orden=id_itinerario, id_ciudad=id_ciudad, id_pais=id_pais, id_agencia=id_agencia, id_paquete=id_paquete)
            except Itinerarios.DoesNotExist:        
                messages.error(request, 'Error con la union de itinerario, ciudad, pais, agencia, paquete')
                return redirect('Show_Detalles_servicios')
            form.save()
            return redirect ('Show_Detalles_servicios')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Detalles_servicios')
    form = Form_Detalles_servicios(instance= obj)
    form.fields['id_itinerario'].widget.attrs['readonly'] = True
    form.fields['id_ciudad'].widget.attrs['readonly'] = True
    form.fields['id_pais'].widget.attrs['readonly'] = True
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    form.fields['id_paquete'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddDetalles_servicios.html',{'form':form})

def Edit_ALO_DET(request, id,id2,id3,id4,id5,id6,id7): #NO TIENE FUNCION, TODAS SUS COLUMNAS SON PK, POR LO QUE ESTAN BLOQUEADAS Y NO SE PUEDEN EDITAR
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
    if request.method == 'POST':
        form = Form_ALO_DET(request.POST, instance= obj)
        try:
            del form.errors['id_detalle_servicio']    
        except:
            pass
        if form.is_valid():

            id_detalle_servicio = form.data['id_detalle_servicio']  
            id_itinerario = form.data['id_itinerario']
            id_paquete = form.data['id_paquete']
            id_agencia = form.data['id_agencia']  
            id_ciudad = form.data['id_ciudad']
            id_pais = form.data['id_pais']
            id_alojamiento = form.data['id_alojamiento']
            try:
                validacion = Detalles_servicios.objects.get(id_detalle_servicio=id_detalle_servicio, id_itinerario=id_itinerario, id_ciudad=id_ciudad, id_pais=id_pais, id_agencia=id_agencia, id_paquete=id_paquete)
            except Detalles_servicios.DoesNotExist:        
                messages.error(request, 'Error con la union de itinerario, ciudad, pais, agencia, paquete y detalle servicio')
                return redirect('Show_ALO_DET')

            Actualizar_ALO_DET(id_detalle_servicio, id_itinerario, id_paquete, id_agencia, id_ciudad, id_pais, id_alojamiento)
            return redirect ('Show_ALO_DET')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_ALO_DET')
    form = Form_ALO_DET(instance= obj)
    form.fields['id_itinerario'].widget.attrs['readonly'] = True
    form.fields['id_ciudad'].widget.attrs['readonly'] = True
    form.fields['id_pais'].widget.attrs['readonly'] = True
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    form.fields['id_paquete'].widget.attrs['readonly'] = True
    form.fields['id_alojamiento'].widget.attrs['readonly'] = True
    form.fields['id_detalle_servicio'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddALO_DET.html',{'form':form})

def Edit_Instrumentos_de_pago(request, id,id2):
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
    if request.method == 'POST':
        form = Form_Instrumentos_de_pago(request.POST, instance= obj)
        if form.is_valid():
            doc_identidad_cliente = form.data['doc_identidad_cliente']
            try:
                validacion = Clientes.objects.get(doc_identidad_o_rif=doc_identidad_cliente)
            except Clientes.DoesNotExist:        
                messages.error(request, 'Cliente no existe')
                return redirect('Show_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') == 'zelle' and form.cleaned_data.get('id_banco')!=None:
                messages.error(request, 'El tipo de instrumento no debe estar vinculado con un banco')
                return redirect('Show_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') == 'zelle' and form.cleaned_data.get('numero_zelle')==None:
                messages.error(request, 'Falto Vincular numero zelle')
                return redirect('Show_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') == 'zelle' and form.cleaned_data.get('email_zelle')==None:
                messages.error(request, 'Falto Vincular Email zelle')
                return redirect('Show_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') != 'zelle' and form.cleaned_data.get('id_banco')==None:
                messages.error(request, 'El tipo de instrumento debe estar vinculado con un banco')
                return redirect('Show_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') != 'zelle' and form.cleaned_data.get('numero_zelle')!=None:
                messages.error(request, 'No se puede vincular numero zelle')
                return redirect('Show_Instrumentos_de_pago')
            if form.cleaned_data.get('tipo_instrumento') != 'zelle' and form.cleaned_data.get('email_zelle')!=None:
                messages.error(request, 'No se puede vincular email zelle')
                return redirect('Show_Instrumentos_de_pago')
            form.save()
            return redirect ('Show_Instrumentos_de_pago')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Instrumentos_de_pago')
    form = Form_Instrumentos_de_pago(instance= obj)
    form.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddInstrumentos_de_pago.html',{'form':form})

def Edit_Paquetes_contrato(request, id):
    try:
        obj = Paquetes_contrato.objects.get(pk=id)
    except Paquetes_contrato.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Paquetes_contrato')
    if request.method == 'POST':
        form = Form_Paquetes_contrato(request.POST, instance= obj)
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
            return redirect('Show_Paquetes_contrato')
    form = Form_Paquetes_contrato(instance= obj)
    return render(request, 'create_edit/AddPaquetes_contrato.html',{'form':form})

def Edit_Formas_de_pago(request, id):
    try:
        obj = Formas_de_pago.objects.get(pk=id)
    except Formas_de_pago.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Formas_de_pago')
    if request.method == 'POST':
        form = Form_Formas_de_pago(request.POST, instance= obj)
        if form.is_valid():

            id_instrumento = form.data['id_instrumento']  
            id_cliente = form.data['id_cliente']
            id_paquete_contrato = form.data['id_paquete_contrato']
            tipo_forma_de_pago = form.data['tipo_forma_de_pago']
            try:
                validacion = Instrumentos_de_pago.objects.get(id_instrumento=id_instrumento, doc_identidad_cliente=id_cliente)
            except Instrumentos_de_pago.DoesNotExist:        
                messages.error(request, 'Error, instrumento de pago y cliente no coinciden')
                return redirect('Show_Formas_de_pago')
            try:
                validacion = Paquetes_contrato.objects.get(numero_factura=id_paquete_contrato)
            except Paquetes_contrato.DoesNotExist:        
                messages.error(request, 'Error, paquete contrato invalido')
                return redirect('Show_Formas_de_pago')

            form.save()
            return redirect ('Show_Formas_de_pago')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Formas_de_pago')
    form = Form_Formas_de_pago(instance= obj)
    return render(request, 'create_edit/AddFormas_de_pago.html',{'form':form})

def Edit_Viajeros(request, id):
    try:
        obj =Viajeros.objects.get(pk=id)
    except Viajeros.DoesNotExist:        
        messages.error(request, 'No existe la entrada')
        return redirect('Show_Viajeros')
    if request.method == 'POST':
        form = Form_Viajeros(request.POST, instance= obj)
        if form.is_valid():

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            try:
                ciudad = Ciudades.objects.get(id_ciudad=id_ciudad, id_pais=id_pais)
            except Ciudades.DoesNotExist:        
                messages.error(request, 'La ciudad no corresponde con el pais')
                return redirect('Show_Viajeros')

            id_paquete_contrato = form.cleaned_data.get('id_paquete_contrato')
            try:
                validacion = Paquetes_contrato.objects.get(numero_factura=id_paquete_contrato)
            except Paquetes_contrato.DoesNotExist:        
                messages.error(request, 'Error, paquete contrato invalido')
                return redirect('Show_Viajeros')

            form.save()
            return redirect ('Show_Viajeros')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Viajeros')
    form = Form_Viajeros(instance= obj)
    form.fields['id_de_identidad'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddViajeros.html',{'form':form})

def Edit_PAI_VIA(request, id,id2):
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
    if request.method == 'POST':
        form = Form_PAI_VIA(request.POST, instance= obj)
        try:
            del form.errors['id_viajero']    
        except:
            pass
        if form.is_valid():
            id_viajero = form.data['id_viajero']  
            id_pais = form.data['id_pais']
            nro_de_pasaporte = form.data['nro_de_pasaporte']
            try:
                validacion = Viajeros.objects.get(id_de_identidad=id_viajero)
            except Viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero invalido')
                return redirect('Show_PAI_VIA')

            Actualizar_PAI_VIA(id_viajero, id_pais, nro_de_pasaporte)
            return redirect ('Show_PAI_VIA')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_PAI_VIA')
    form = Form_PAI_VIA(instance= obj)
    form.fields['id_viajero'].widget.attrs['readonly'] = True
    form.fields['id_pais'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddPAI_VIA.html',{'form':form})

def Edit_Registro_viajeros(request, id,id2):
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
    if request.method == 'POST':
        form = Form_Registro_viajeros(request.POST, instance= obj)
        try:
            del form.errors['id_agencia']    
        except:
            pass
        if form.is_valid():
            id_agencia = form.data['id_agencia']  
            id_viajero = form.data['id_viajero']
            f_registro = form.data['f_registro']
            nro_registro = form.data['nro_registro']
            try:
                validacion = Viajeros.objects.get(id_de_identidad=id_viajero)
            except Viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero invalido')
                return redirect('Show_Registro_viajeros')
            try:
                validacion = Agencias_de_viajes.objects.get(id_agencia=id_agencia)
            except Agencias_de_viajes.DoesNotExist:        
                messages.error(request, 'Error, Agencia invalida')
                return redirect('Show_Registro_viajeros')

            Actualizar_Registro_viajeros(id_agencia, id_viajero, f_registro, nro_registro)
            return redirect ('Show_Registro_viajeros')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Registro_viajeros')
    form = Form_Registro_viajeros(instance= obj)
    form.fields['id_viajero'].widget.attrs['readonly'] = True
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    
    return render(request, 'create_edit/AddRegistro_viajeros.html',{'form':form})

def Edit_Detalle_viajeros(request, id,id2,id3): #NO TIENE FUNCION, TODAS SUS COLUMNAS SON PK, POR LO QUE ESTAN BLOQUEADAS Y NO SE PUEDEN EDITAR
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
    if request.method == 'POST':
        form = Form_Detalle_viajeros(request.POST, instance= obj)
        try:
            del form.errors['id_viajero']    
        except:
            pass
        if form.is_valid():
            id_viajero = form.data['id_viajero']
            id_agencia = form.data['id_agencia']
            id_paquete_contrato = form.data['id_paquete_contrato']
            try:
                validacion = Registro_viajeros.objects.get(id_agencia=id_agencia, id_viajero=id_viajero)
            except Registro_viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero no pertenece a la agencia')
                return redirect('Show_Detalle_viajeros')
            try:
                validacion = Paquetes_contrato.objects.get(numero_factura=id_paquete_contrato)
            except Paquetes_contrato.DoesNotExist:        
                messages.error(request, 'Error, Paquete invalido')
                return redirect('Show_Detalle_viajeros')

            Actualizar_Detalle_viajero(id_viajero, id_agencia, id_paquete_contrato)
            return redirect ('Show_Detalle_viajeros')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Detalle_viajeros')
    form = Form_Detalle_viajeros(instance= obj)
    form.fields['id_viajero'].widget.attrs['readonly'] = True
    form.fields['id_agencia'].widget.attrs['readonly'] = True
    form.fields['id_paquete_contrato'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddDetalle_viajeros.html',{'form':form})
    
def Edit_Participantes(request, id,id2):
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
    if request.method == 'POST':
        form = Form_Participantes(request.POST, instance= obj)
        if form.is_valid():
            id_via_agencia = form.data['id_via_agencia']
            id_via_viajero = form.data['id_via_viajero']
            id_cli_cliente = form.data['id_cli_cliente']  
            id_cli_agencia = form.data['id_cli_agencia']

            try:
                validacion = Registro_viajeros.objects.get(id_agencia=id_via_agencia, id_viajero=id_via_viajero)
            except Registro_viajeros.DoesNotExist:        
                messages.error(request, 'Error, Viajero no pertenece a la agencia')
                return redirect('Show_Participantes')
            try:
                validacion = Registro_clientes.objects.get(id_cliente=id_cli_cliente, id_agencia=id_cli_agencia)
            except Registro_clientes.DoesNotExist:        
                messages.error(request, 'Error, Cliente no pertenece a la agencia')
                return redirect('Show_Participantes')
            form.save()
            return redirect ('Show_Participantes')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Participantes')
    form = Form_Participantes(instance= obj)
    form.fields['id_rally'].widget.attrs['readonly'] = True
    return render(request, 'create_edit/AddParticipantes.html',{'form':form})

def Edit_Puntuaciones(request, id):
    try:
        obj = Puntuaciones.objects.get(id_puntuacion=id)
    except Puntuaciones.DoesNotExist:        
        messages.error(request, 'No existe la entrada2')
        return redirect('Show_Puntuaciones')
    if request.method == 'POST':
        form = Form_Puntuaciones(request.POST, instance= obj)
        if form.is_valid():

            id_paquete_contrato = form.cleaned_data.get('id_paquete_contrato')
            try:
                validacion = Paquetes_contrato.objects.get(numero_factura=id_paquete_contrato)
            except Paquetes_contrato.DoesNotExist:        
                messages.error(request, 'Error, paquete contrato invalido')
                return redirect('Show_Puntuaciones')

            id_ciudad = form.cleaned_data.get('id_ciudad')
            id_pais = form.cleaned_data.get('id_pais')
            id_atraccion = form.cleaned_data.get('id_atraccion')
            try:
                atraccion = Atracciones.objects.get(id_ciudad=id_ciudad, id_pais=id_pais, id_atraccion=id_atraccion)
            except Atracciones.DoesNotExist:        
                messages.error(request, 'Error con la union de ciudad, pais y atraccion, verificar integridad')
                return redirect('Show_Puntuaciones')

            form.save()
            return redirect ('Show_Puntuaciones')
        else:
            messages.error(request, 'Entrada Invalida')
            return redirect('Show_Puntuaciones')
    form = Form_Puntuaciones(instance= obj)
    return render(request, 'create_edit/AddPuntuaciones.html',{'form':form})


#Otros--------------------------------------------------------------------------------------------------------------------

def Registrar_nuevo_cliente(request):
    if request.method == 'POST':
        form = Form_nuevo_registro_cliente(request.POST)
        cedula = form.data['cedula']
        tipo = form.data['tipo']
        nombre = form.data['nombre']
        apellido1 = form.data['apellido1']
        apellido2 = form.data['apellido2']
        agencia = form.data['agencia']
        f_registro = date.today()
        if Crear_nuevo_Cliente(cedula, tipo, nombre, apellido1, apellido2) == 1:
            messages.error(request, 'Cliente ya agregado en sistema')
            return redirect('Registrar_nuevo_cliente')
        if Crear_nuevo_Registro_clientes(cedula, agencia, f_registro) == 1:
            messages.error(request, 'Criente ya registrado en agencia de viajes')
            return redirect('Registrar_nuevo_cliente')
        
        form_i = Form_Instrumentos_de_pago(initial={'doc_identidad_cliente': cedula})
        form_i.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
        return render(request, 'rn_instrumento_pago.html',{'form':form_i})
    form = Form_nuevo_registro_cliente()
    return render(request, 'registrar_nuevo_cliente.html',{'form':form})

def Rn_intrumento_1(request):
    form = Form_Instrumentos_de_pago(request.POST)
    if form.data['tipo_instrumento'] == 'zelle' and form.data['id_banco']!='':
        messages.error(request, 'El tipo de instrumento no debe estar vinculado con un banco')
        return redirect('Show_Clientes')
    if form.data['tipo_instrumento'] == 'zelle' and form.data['numero_zelle']=='':
        messages.error(request, 'Falto Vincular numero zelle')
        return redirect('Show_Clientes')
    if form.data['tipo_instrumento'] == 'zelle' and form.data['email_zelle']=='':
        messages.error(request, 'Falto Vincular Email zelle')
        return redirect('Show_Clientes')
    if form.data['tipo_instrumento'] != 'zelle' and form.data['id_banco']=='':
        messages.error(request, 'El tipo de instrumento debe estar vinculado con un banco')
        return redirect('Show_Clientes')
    if form.data['tipo_instrumento'] != 'zelle' and form.data['numero_zelle']!='':
        messages.error(request, 'No se puede vincular numero zelle')
        return redirect('Show_Clientes')
    if form.data['tipo_instrumento'] != 'zelle' and form.data['email_zelle']!='':
        messages.error(request, 'No se puede vincular email zelle')
        return redirect('Show_Clientes')
    try:
        form.save()
    except:
        messages.error(request, 'Error al registrar instrumento de pago')
    return redirect ('Show_Clientes')

def Rn_intrumento_2(request):
    form = Form_Instrumentos_de_pago(request.POST)
    if form.data['tipo_instrumento'] == 'zelle' and form.data['id_banco']!='':
        messages.error(request, 'El tipo de instrumento no debe estar vinculado con un banco')
        cedula = form.data['doc_identidad_cliente']
        form_i = Form_Instrumentos_de_pago(initial={'doc_identidad_cliente': cedula})
        form_i.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
        return render(request, 'rn_instrumento_pago.html',{'form':form_i})
    if form.data['tipo_instrumento'] == 'zelle' and form.data['numero_zelle']=='':
        messages.error(request, 'Falto Vincular numero zelle')
        cedula = form.data['doc_identidad_cliente']
        form_i = Form_Instrumentos_de_pago(initial={'doc_identidad_cliente': cedula})
        form_i.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
        return render(request, 'rn_instrumento_pago.html',{'form':form_i})
    if form.data['tipo_instrumento'] == 'zelle' and form.data['email_zelle']=='':
        messages.error(request, 'Falto Vincular Email zelle')
        cedula = form.data['doc_identidad_cliente']
        form_i = Form_Instrumentos_de_pago(initial={'doc_identidad_cliente': cedula})
        form_i.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
        return render(request, 'rn_instrumento_pago.html',{'form':form_i})
    if form.data['tipo_instrumento'] != 'zelle' and form.data['id_banco']=='':
        messages.error(request, 'El tipo de instrumento debe estar vinculado con un banco')
        cedula = form.data['doc_identidad_cliente']
        form_i = Form_Instrumentos_de_pago(initial={'doc_identidad_cliente': cedula})
        form_i.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
        return render(request, 'rn_instrumento_pago.html',{'form':form_i})
    if form.data['tipo_instrumento'] != 'zelle' and form.data['numero_zelle']!='':
        messages.error(request, 'No se puede vincular numero zelle')
        cedula = form.data['doc_identidad_cliente']
        form_i = Form_Instrumentos_de_pago(initial={'doc_identidad_cliente': cedula})
        form_i.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
        return render(request, 'rn_instrumento_pago.html',{'form':form_i})
    if form.data['tipo_instrumento'] != 'zelle' and form.data['email_zelle']!='':
        messages.error(request, 'No se puede vincular email zelle')
        cedula = form.data['doc_identidad_cliente']
        form_i = Form_Instrumentos_de_pago(initial={'doc_identidad_cliente': cedula})
        form_i.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
        return render(request, 'rn_instrumento_pago.html',{'form':form_i})
    try:
        form.save()
    except:
        messages.error(request, 'Error al registrar instrumento de pago')
    cedula = form.data['doc_identidad_cliente']
    form_i = Form_Instrumentos_de_pago(initial={'doc_identidad_cliente': cedula})
    form_i.fields['doc_identidad_cliente'].widget.attrs['readonly'] = True
    return render(request, 'rn_instrumento_pago.html',{'form':form_i})

def Registrar_nuevo_viajero(request):
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

        if Crear_nuevo_viajero(cedula, ciudad, pais_de_ciudad, paquete, nombre1, apellido1, apellido2, sexo, f_nacimento, nombre2) == 1:
            messages.error(request, 'Error al agregar Viajero')
            return redirect('Registrar_nuevo_viajero')
        if Crear_nuevo_PAI_VIA(cedula, pais, pasaporte) == 1:
            messages.error(request, 'Error al agregar pasaporte viajero')
            return redirect('Registrar_nuevo_viajero')
        if Crear_Registro_viajeros(agencia, cedula, f_registro, '1') ==1:
            messages.error(request, 'Error al registrar viajero')
            return redirect('Registrar_nuevo_viajero')

        return redirect('Show_Viajeros')
    
    form = Form_nuevo_registro_viajero()
    return render(request, 'registrar_nuevo_viajero.html',{'form':form})

def Registrar_nuevo_socio_proveedor(request):
    if request.method == 'POST':
        form = Form_nuevo_socio_proveedor(request.POST)

        nombre = form.data['nombre']
        tipo = form.data['tipo']
        alojamiento = form.data['alojamiento']
        agencia = form.data['agencia']
        f_inicio = form.data['f_inicio']
        f_fin = form.data['f_fin']


        if form.is_valid():
            if (form.cleaned_data.get('f_fin')!=None) and (form.cleaned_data.get('f_fin') < form.cleaned_data.get('f_inicio')):
                messages.error(request, 'Fecha Fin debe ser mayor a fecha inicio')
                return redirect('Registrar_nuevo_socio_proveedor')
        
        if Crear_nuevo_Proveedor(alojamiento,nombre,tipo) == 1:
            messages.error(request, 'Error al agregar proveedor')
            return redirect('Show_Proveedores')

        pro = Proveedores.objects.get(nombre_proveedor=nombre)
        
        if Crear_nuevo_PRO_AGE(agencia,pro.id_proveedor,f_inicio,f_fin) == 1:
            messages.error(request, 'Error al vincular la agencia con el proveedor')
            return redirect('Show_pro_age')

        return redirect('Show_pro_age')
    
    form = Form_nuevo_socio_proveedor()
    return render(request, 'registrar_nuevo_socio_proveedor.html',{'form':form})


# Nuevo Paquete --------------------------------------------------------------------------------------------------------------------------------

def nuevo_paquete_view(request):
    class basico:
        agencia = 1
    return render(request, 'base_paquete.html',{'basico':basico})



def paquete_datos_basicos(request): #Paquete - Itinerario
    if request.method == 'POST':
            form = Form_nuevo_paquete_basico(request.POST)

            agencia = form.data['agencia']
            nombre = form.data['nombre']
            duracion = form.data['Duracion']
            personas = form.data['personas']
            descripcion = form.data['descripcion']
            
            try:
                disponible = form.data['disponible']
            except:
                disponible = ''

            if Crear_nuevo_paquete_datos_basicos(agencia, nombre, duracion, descripcion, disponible, personas)==1:
                messages.error(request, 'Error al crear paquete')
                return render(request, 'nuevo_paquete/datos_basicos.html',{'form':form})
            
            id_paquete = Paquetes.objects.latest('id_paquete')

            form = front_itinerario(1, id_paquete.id_paquete, agencia, duracion)
            return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})

    form = Form_nuevo_paquete_basico()
    return render(request, 'nuevo_paquete/datos_basicos.html',{'form':form})


def paquete_itinerario_a(request):  #Itinerario - Atraccion
    if request.method == 'POST':
            form = Form_nuevo_paquete_itinerario(request.POST)

            tiempo = form.data['tiempo']
            agencia = form.data['agencia']
            paquete = form.data['paquete']

            if int(tiempo) == 0:
                form = front_calendario(paquete, agencia)
                return render(request, 'nuevo_paquete/paq_calendario.html',{'form':form})

            orden = form.data['orden']
            
            ciudad = form.data['ciudad']
            pais = Ciudades.objects.get(id_ciudad=ciudad)
            pais = Paises.objects.get(nombre_pais=pais.id_pais)
            pais = pais.id_pais

            if int(form.data['max']) < int(tiempo):
                messages.error(request, 'El tiempo maximo debe ser igual o menor al tiempo de estadia')
                max = form.data['max']
                form = front_itinerario(orden, paquete, agencia, max)
                return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})

            max = int(form.data['max']) - int(tiempo)

            try:
                Crear_Itinerarios(orden, ciudad, pais, agencia, paquete, tiempo)
            except:
                messages.error(request, 'Error al crear Itinerario')
                max = form.data['max']
                form = front_itinerario(orden, paquete, agencia, max)
                return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})

            form = front_atraccion(ciudad, 1, orden, pais, agencia, paquete, max)
            return render(request, 'nuevo_paquete/paq_atr_itn.html',{'form':form})

def paquete_itinerario_c(request): #Itinerario - Itinerario
    if request.method == 'POST':
            form = Form_nuevo_paquete_itinerario(request.POST)

            agencia = form.data['agencia']
            paquete = form.data['paquete']
            tiempo = form.data['tiempo']

            if int(tiempo) == 0:
                form = front_calendario(paquete, agencia)
                return render(request, 'nuevo_paquete/paq_calendario.html',{'form':form})

            orden = form.data['orden']
            max = int(form.data['max']) - int(tiempo)
            ciudad = form.data['ciudad']
            pais = Ciudades.objects.get(id_ciudad=ciudad)
            pais = Paises.objects.get(nombre_pais=pais.id_pais)
            pais = pais.id_pais   

            if int(form.data['max']) < int(tiempo):
                messages.error(request, 'El tiempo maximo debe ser igual o menor al tiempo de estadia')
                max = form.data['max']
                form = front_itinerario(orden, paquete, agencia, max)
                return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})        

            try:
                Crear_Itinerarios(orden, ciudad, pais, agencia, paquete, tiempo)
            except:
                messages.error(request, 'Error al crear Itinerario')
                max = form.data['max']
                form = front_itinerario(orden, paquete, agencia, max)
                return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})

            orden = int(form.data['orden']) + 1
            
            #----------------------------------------------------------------------------
            form = front_itinerario(orden, paquete, agencia, max)
            return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})

def paquete_itinerario_d(request): #Itienerario - Calendario
    if request.method == 'POST':
            form = Form_nuevo_paquete_itinerario(request.POST)

            agencia = form.data['agencia']
            paquete = form.data['paquete']
            tiempo = form.data['tiempo']

            if int(tiempo) == 0:
                form = front_calendario(paquete, agencia)
                return render(request, 'nuevo_paquete/paq_calendario.html',{'form':form})

            orden = form.data['orden']
            max = int(form.data['max']) - int(tiempo)
            ciudad = form.data['ciudad']
            pais = Ciudades.objects.get(id_ciudad=ciudad)
            pais = Paises.objects.get(nombre_pais=pais.id_pais)
            pais = pais.id_pais        

            if int(form.data['max']) < int(tiempo):
                messages.error(request, 'El tiempo maximo debe ser igual o menor al tiempo de estadia')
                max = form.data['max']
                form = front_itinerario(orden, paquete, agencia, max)
                return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})     

            try:
                Crear_Itinerarios(orden, ciudad, pais, agencia, paquete, tiempo)
            except:
                messages.error(request, 'Error al crear Itinerario')
                max = form.data['max']
                form = front_itinerario(orden, paquete, agencia, max)
                return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})

            orden = int(form.data['orden']) + 1
            
            #----------------------------------------------------------------------------

            form = front_calendario(paquete, agencia)
            return render(request, 'nuevo_paquete/paq_calendario.html',{'form':form})


def paquete_atr_itn_a(request): #Atraccion - Itinerario
    if request.method == 'POST':
            form = Form_nuevo_paquete_itn_atr_post(request.POST)

            agencia = form.data['agencia']
            paquete = form.data['paquete']
            ciudad = form.data['ciudad']        
            pais = form.data['pais']            
            atraccion = form.data['atraccion']  
            orden = form.data['orden']          
            itn = form.data['itn'] 

            if atraccion != '':          
                try:
                    Crear_ITN_ATR(itn, ciudad, pais, agencia, paquete, atraccion, ciudad, pais, orden)
                except:
                    messages.error(request, 'Error al vincular atraccion')
                    form = front_atraccion(ciudad, orden, itn, pais, agencia, paquete, max)
                    return render(request, 'nuevo_paquete/paq_atr_itn.html',{'form':form})

            itn = int(form.data['itn']) + 1
            max = form.data['max']
            form = front_itinerario(itn, paquete, agencia, max)
            return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})

def paquete_atr_itn_b(request): #Atraccion - Atraccion
    if request.method == 'POST':
            form = Form_nuevo_paquete_itn_atr_post(request.POST)

            agencia = form.data['agencia']
            paquete = form.data['paquete']

            ciudad = form.data['ciudad']        
            pais = form.data['pais']            
            atraccion = form.data['atraccion']

            orden = form.data['orden']

            itn = form.data['itn']       

            max = form.data['max']       

            if atraccion != '':   
                try:
                    Crear_ITN_ATR(itn, ciudad, pais, agencia, paquete, atraccion, ciudad, pais, orden)
                except:
                    messages.error(request, 'Error al vincular atraccion')
                    form = front_atraccion(ciudad, orden, itn, pais, agencia, paquete, max)
                    return render(request, 'nuevo_paquete/paq_atr_itn.html',{'form':form})
                orden = int(form.data['orden']) + 1 

            form = front_atraccion(ciudad, orden, itn, pais, agencia, paquete, max)
            return render(request, 'nuevo_paquete/paq_atr_itn.html',{'form':form})

def paquete_atr_itn_c(request): #Atraccion - Detalle
    if request.method == 'POST':
            form = Form_nuevo_paquete_itn_atr_post(request.POST)

            agencia = form.data['agencia']
            paquete = form.data['paquete']

            ciudad = form.data['ciudad']        
            pais = form.data['pais']            
            atraccion = form.data['atraccion']  #dato ya no me interesa

            orden = form.data['orden'] 

            itn = form.data['itn']       

            max = form.data['max']       
            
            if atraccion != '':   
                try:
                    Crear_ITN_ATR(itn, ciudad, pais, agencia, paquete, atraccion, ciudad, pais, orden)
                except:
                    messages.error(request, 'Error al vincular atraccion')
                    form = front_atraccion(ciudad, orden, itn, pais, agencia, paquete, max)
                    return render(request, 'nuevo_paquete/paq_atr_itn.html',{'form':form})

            form = front_detalle(itn, ciudad, pais, agencia, paquete, max)
            return render(request, 'nuevo_paquete/paq_det_ser.html',{'form':form})

def paquete_atr_itn_d(request): #Atraccion - Calendario
    if request.method == 'POST':
            form = Form_nuevo_paquete_itn_atr_post(request.POST)

            agencia = form.data['agencia']
            paquete = form.data['paquete']

            ciudad = form.data['ciudad']        
            pais = form.data['pais']            
            atraccion = form.data['atraccion']  #dato ya no me interesa

            orden = form.data['orden'] 

            itn = form.data['itn']       

            max = form.data['max']   

            if atraccion != '':   
                try:
                    Crear_ITN_ATR(itn, ciudad, pais, agencia, paquete, atraccion, ciudad, pais, orden)
                except:
                    messages.error(request, 'Error al vincular atraccion')
                    form = front_atraccion(ciudad, orden, itn, pais, agencia, paquete, max)
                    return render(request, 'nuevo_paquete/paq_atr_itn.html',{'form':form})
            
            form = front_calendario(paquete, agencia)
            return render(request, 'nuevo_paquete/paq_calendario.html',{'form':form})


def paquete_det_ser_a(request): #Detalle - (alojamiento) - Itinerario
    if request.method == 'POST':
            form = Form_nuevo_paquete_itinerario(request.POST)

            itinerario = form.data['itinerario']
            max = form.data['max']
            paquete = form.data['paquete']
            agencia = form.data['agencia']

            tipo = form.data['tipo']
            descripcion = form.data['descripcion']
            
            try:
                comida = form.data['comida']
            except:
                comida = ''
            
            ciudad = form.data['ciudad']   
            pais = form.data['pais']          

            if tipo != '-----':
                try:
                    Crear_nuevo_paquete_detalle_servicio(itinerario, paquete, agencia, ciudad, pais, tipo, descripcion, comida)
                except:
                    messages.error(request, 'Error al crear Detalle servicio')
                    form = front_detalle(itinerario, ciudad, pais, agencia, paquete, max)
                    return render(request, 'nuevo_paquete/paq_det_ser.html',{'form':form})

            #------------------------------------------------------------------------------------

            if tipo == 'alojamiento':
                id_detalle = Detalles_servicios.objects.latest('id_detalle_servicio')
                form = front_alojamiento(ciudad, id_detalle.id_detalle_servicio, itinerario, paquete, agencia, max, pais)
                return render(request, 'nuevo_paquete/paq_alo_det.html',{'form':form})
            
            #----------------------------------------------------------------------------

            itinerario = int(form.data['itinerario']) + 1

            form = front_itinerario(itinerario, paquete, agencia, max)
            return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})

def paquete_det_ser_b(request): #Detalle - (Alojamiento) - Detalle
    if request.method == 'POST':
            form = Form_nuevo_paquete_itinerario(request.POST)

            itinerario = form.data['itinerario']
            max = form.data['max']
            paquete = form.data['paquete']
            agencia = form.data['agencia']

            tipo = form.data['tipo']
            descripcion = form.data['descripcion']
            try:
                comida = form.data['comida']
            except:
                comida = ''
            
            ciudad = form.data['ciudad']   
            pais = form.data['pais']          
            
            if tipo != '-----':
                try:
                    Crear_nuevo_paquete_detalle_servicio(itinerario, paquete, agencia, ciudad, pais, tipo, descripcion, comida)
                except:
                    messages.error(request, 'Error al crear Detalle servicio')
                    form = front_detalle(itinerario, ciudad, pais, agencia, paquete, max)
                    return render(request, 'nuevo_paquete/paq_det_ser.html',{'form':form})

            if tipo == 'alojamiento':
                id_detalle = Detalles_servicios.objects.latest('id_detalle_servicio')
                form = front_alojamiento(ciudad, id_detalle.id_detalle_servicio, itinerario, paquete, agencia, max, pais)
                return render(request, 'nuevo_paquete/paq_alo_det.html',{'form':form})
            
            #----------------------------------------------------------------------------

            form = front_detalle(itinerario, ciudad, pais, agencia, paquete, max)
            return render(request, 'nuevo_paquete/paq_det_ser.html',{'form':form})

def paquete_det_ser_c(request): #Detalle - (alojamiento) - Calendario
    if request.method == 'POST':
            form = Form_nuevo_paquete_itinerario(request.POST)

            itinerario = form.data['itinerario']
            max = form.data['max']
            paquete = form.data['paquete']
            agencia = form.data['agencia']

            tipo = form.data['tipo']
            descripcion = form.data['descripcion']
            try:
                comida = form.data['comida']
            except:
                comida = ''
            
            ciudad = form.data['ciudad']   
            pais = form.data['pais']  

            if tipo != '-----':
                try:
                    Crear_nuevo_paquete_detalle_servicio(itinerario, paquete, agencia, ciudad, pais, tipo, descripcion, comida)
                except:
                    messages.error(request, 'Error al crear Detalle servicio')
                    form = front_detalle(itinerario, ciudad, pais, agencia, paquete, max)
                    return render(request, 'nuevo_paquete/paq_det_ser.html',{'form':form})

            if tipo == 'alojamiento':
                id_detalle = Detalles_servicios.objects.latest('id_detalle_servicio')
                form = front_alojamiento(ciudad, id_detalle.id_detalle_servicio, itinerario, paquete, agencia, max, pais)
                return render(request, 'nuevo_paquete/paq_alo_det.html',{'form':form})
            
            #----------------------------------------------------------------------------

            form = front_calendario(paquete, agencia)
            return render(request, 'nuevo_paquete/paq_calendario.html',{'form':form})


def paquete_alo_det_a(request): #Alojamiento - Itinerario
    if request.method == 'POST':
            form = Form_nuevo_paquete_alo_det_post(request.POST)

            detalle = form.data['detalle']
            itn = form.data['itn']
            max = form.data['max']
            paquete = form.data['paquete']
            agencia = form.data['agencia']
            alojamiento = form.data['alojamiento']
            
            ciudad = form.data['ciudad']   
            pais = form.data['pais']          

            if alojamiento != '':
                try:
                    Crear_ALO_DET(detalle, itn, paquete, agencia, ciudad, pais, alojamiento)
                except:
                    messages.error(request, 'Error al vincular alojamiento')
                    form = front_alojamiento(ciudad, detalle, itn, paquete, agencia, max)
                    return render(request, 'nuevo_paquete/paq_alo_det.html',{'form':form})
            
            #----------------------------------------------------------------------------

            itinerario = int(form.data['itn']) + 1
            form = front_itinerario(itinerario, paquete, agencia, max)
            return render(request, 'nuevo_paquete/itinerario_paq.html',{'form':form})

def paquete_alo_det_b(request): #Alojamiento - Calendario
    if request.method == 'POST':
            form = Form_nuevo_paquete_alo_det_post(request.POST)

            detalle = form.data['detalle']
            itn = form.data['itn']
            max = form.data['max']
            paquete = form.data['paquete']
            agencia = form.data['agencia']
            alojamiento = form.data['alojamiento']
            
            ciudad = form.data['ciudad']   
            pais = form.data['pais']          

            if alojamiento != '':
                try:
                    Crear_ALO_DET(detalle, itn, paquete, agencia, ciudad, pais, alojamiento)
                except:
                    messages.error(request, 'Error al vincular alojamiento')
                    form = front_alojamiento(ciudad, detalle, itn, paquete, agencia, max)
                    return render(request, 'nuevo_paquete/paq_alo_det.html',{'form':form})
            
            #----------------------------------------------------------------------------

            form = front_calendario(paquete, agencia)
            return render(request, 'nuevo_paquete/paq_calendario.html',{'form':form})

def paquete_alo_det_c(request): #Alojamiento - Detalle
    if request.method == 'POST':
            form = Form_nuevo_paquete_alo_det_post(request.POST)

            detalle = form.data['detalle']
            itn = form.data['itn']
            max = form.data['max']
            paquete = form.data['paquete']
            agencia = form.data['agencia']
            alojamiento = form.data['alojamiento']
            
            ciudad = form.data['ciudad']   
            pais = form.data['pais']          

            if alojamiento != '':
                try:
                    Crear_ALO_DET(detalle, itn, paquete, agencia, ciudad, pais, alojamiento)
                except:
                    messages.error(request, 'Error al vincular alojamiento')
                    form = front_alojamiento(ciudad, detalle, itn, paquete, agencia, max)
                    return render(request, 'nuevo_paquete/paq_alo_det.html',{'form':form})
            
            #----------------------------------------------------------------------------

            form = front_detalle(itn, ciudad, pais, agencia, paquete, max)
            return render(request, 'nuevo_paquete/paq_det_ser.html',{'form':form})


def paquete_cal_a(request): #Calendario - Precio
    if request.method == 'POST':
            form = Form_nuevo_paquete_calendario(request.POST)

            
            paquete = form.data['paquete']
            agencia = form.data['agencia']

            salida = form.data['salida']
            descripcion = form.data['descripcion']

            try:
                Crear_Calendarios_anuales(salida, paquete, agencia, descripcion)
            except:
                messages.error(request, 'Fecha ya vinculada')
                form = front_calendario(paquete, agencia)
                return render(request, 'nuevo_paquete/paq_calendario.html',{'form':form})
            
            #----------------------------------------------------------------------------

            form = Form_nuevo_paquete_precio(initial={'paquete': paquete, 'agencia': agencia})
            form.fields['paquete'].widget.attrs['hidden'] = True
            form.fields['agencia'].widget.attrs['hidden'] = True
            return render(request, 'nuevo_paquete/paq_precio.html',{'form':form})

def paquete_cal_b(request): #Calendario - Calendario
    if request.method == 'POST':
            form = Form_nuevo_paquete_calendario(request.POST)

            
            paquete = form.data['paquete']
            agencia = form.data['agencia']

            salida = form.data['salida']
            descripcion = form.data['descripcion']

            try:
                Crear_Calendarios_anuales(salida, paquete, agencia, descripcion)
            except:
                messages.error(request, 'Fecha ya vinculada')
                form = front_calendario(paquete, agencia)
                return render(request, 'nuevo_paquete/paq_calendario.html',{'form':form})
            
            #----------------------------------------------------------------------------

            form = front_calendario(paquete, agencia)
            return render(request, 'nuevo_paquete/paq_calendario.html',{'form':form})


def paquete_precio(request): #Precio - FIN
    if request.method == 'POST':
            form = Form_nuevo_paquete_precio(request.POST)

            
            paquete = form.data['paquete']
            agencia = form.data['agencia']

            inicio = form.data['inicio']

            try:
                fin = form.data['fin']
            except:
                fin = ''
            
            valor = form.data['valor']

            if form.is_valid():
                if (form.cleaned_data.get('fin')!=None) and (form.cleaned_data.get('fin') < form.cleaned_data.get('inicio')):
                    messages.error(request, 'Fecha Fin debe ser mayor a fecha inicio')
                    form = Form_nuevo_paquete_precio(initial={'paquete': paquete, 'agencia': agencia})
                    form.fields['paquete'].widget.attrs['hidden'] = True
                    form.fields['agencia'].widget.attrs['hidden'] = True    
                    return render(request, 'nuevo_paquete/paq_precio.html',{'form':form})

            try:
                Crear_Precio_paquete(inicio, paquete, agencia, fin, valor)
            except:
                messages.error(request, 'Error al colocar el precio')
                form = Form_nuevo_paquete_precio(initial={'paquete': paquete, 'agencia': agencia})
                form.fields['paquete'].widget.attrs['hidden'] = True
                form.fields['agencia'].widget.attrs['hidden'] = True    
                return render(request, 'nuevo_paquete/paq_precio.html',{'form':form})
            
            #----------------------------------------------------------------------------

            return redirect('paquete_fin',paquete)

def paquete_fin(request, id):
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
    
    return render(request, 'nuevo_paquete/paquete_fin.html',{       'paq':paquete, 
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


# -------------------------------------------------------

def  front_itinerario(orden, paquete, agencia, max):
    form = Form_nuevo_paquete_itinerario(initial={'orden': orden, 'paquete': paquete, 'agencia': agencia, 'max': max})
    form.fields['orden'].widget.attrs['readonly'] = True
    form.fields['paquete'].widget.attrs['hidden'] = True
    form.fields['agencia'].widget.attrs['hidden'] = True
    form.fields['max'].widget.attrs['readonly'] = True
    return form

def front_calendario(paquete, agencia):
    form = Form_nuevo_paquete_calendario(initial={'paquete': paquete, 'agencia': agencia})
    form.fields['paquete'].widget.attrs['hidden'] = True
    form.fields['agencia'].widget.attrs['hidden'] = True
    return form

def front_atraccion(ciudad, orden, itn, pais, agencia, paquete, max):
    form = Form_nuevo_paquete_itn_atr(ciudad, initial={'itn': itn, 'orden': orden, 'ciudad': ciudad, 'pais': pais, 'agencia': agencia, 'paquete': paquete, 'max': max})
    form.fields['orden'].widget.attrs['readonly'] = True
    form.fields['itn'].widget.attrs['readonly'] = True
    form.fields['ciudad'].widget.attrs['hidden'] = True
    form.fields['pais'].widget.attrs['hidden'] = True
    form.fields['agencia'].widget.attrs['hidden'] = True
    form.fields['paquete'].widget.attrs['hidden'] = True
    form.fields['max'].widget.attrs['hidden'] = True
    return form

def front_detalle(itn, ciudad, pais, agencia, paquete, max):
    form = Form_nuevo_paquete_det_ser(initial={'itinerario': itn, 'ciudad': ciudad, 'pais': pais, 'agencia': agencia, 'paquete': paquete, 'max': max})
    form.fields['itinerario'].widget.attrs['readonly'] = True
    form.fields['ciudad'].widget.attrs['hidden'] = True
    form.fields['pais'].widget.attrs['hidden'] = True
    form.fields['agencia'].widget.attrs['hidden'] = True
    form.fields['paquete'].widget.attrs['hidden'] = True
    form.fields['max'].widget.attrs['hidden'] = True
    return form

def front_alojamiento(ciudad, detalle, itinerario, paquete, agencia, max, pais):
    form = Form_nuevo_paquete_alo_det(ciudad, initial={'detalle': detalle, 'itn': itinerario, 'paquete': paquete, 'agencia': agencia, 'max': max, 'pais': pais, 'ciudad': ciudad})
    form.fields['detalle'].widget.attrs['hidden'] = True
    form.fields['itn'].widget.attrs['hidden'] = True
    form.fields['paquete'].widget.attrs['hidden'] = True
    form.fields['agencia'].widget.attrs['hidden'] = True
    form.fields['max'].widget.attrs['hidden'] = True
    form.fields['pais'].widget.attrs['hidden'] = True
    form.fields['ciudad'].widget.attrs['hidden'] = True
    return form


