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