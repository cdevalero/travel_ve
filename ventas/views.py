from django import http
from ventas.forms import *
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import timedelta

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
                except Itinerarios.DoesNotExist: 
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
                                    pre.valor = int(int(pre.valor)*1.22)

            return render(request, 'ver_paquetes.html',{'paquetes':paquete, 'ciudades':city, 'precio':precio, 'itinerarios':itinerarios,'pais': pais})
    form = Form_Buscar_paquerte()
    return render(request, 'buscar.html',{'form':form})

