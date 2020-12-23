from django.contrib import admin
from django.urls import path, include
from .views import *


'''
    TEST
    path('', Test_Show, name="Test_Show"),
    path('Test_ShowDepartamentos/', Test_ShowDepartamentos, name="Test_ShowDepartamentos"),
    path('Test_ShowEmpleados/', Test_ShowEmpleados, name="Test_ShowEmpleados"),
'''

urlpatterns = [

    path('', Show_Ciudades, name="Show_Ciudades"),
    path('agencias_de_viajes/', Show_Agencias_de_viajes, name="Show_Agencias_de_viajes"),
    path('age_age/', Show_AGE_AGE, name="Show_AGE_AGE"),

]