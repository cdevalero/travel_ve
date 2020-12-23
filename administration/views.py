from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from datetime import timedelta

'''
def Test_ShowDepartamentos(request):
    obj = Test_Departamentos.objects.all()
    return render(request, 'test/ShowDepartamentos.html', {'obj': obj})

def Test_ShowEmpleados(request):
    obj = Test_Empleados.objects.all()
    return render(request, 'test/ShowEmpleados.html', {'obj': obj})
'''

def Test_Show(request):
    return render(request, 'base_admin.html')

def Show_Ciudades(request):
    obj = Ciudades.objects.all()
    return render(request, 'show/ShowCiudades.html', {'obj': obj})

def Show_Agencias_de_viajes(request):
    obj = Agencias_de_viajes.objects.all()
    return render(request, 'show/ShowAgencias_de_viajes.html', {'obj': obj})

def Show_AGE_AGE(request):
    obj = AGE_AGE.objects.all()
    return render(request, 'show/ShowAGE_AGE.html', {'obj': obj})