from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # TEST
    path('', Test_Show, name="Test_Show"),
    #path('Test_ShowDepartamentos/', Test_ShowDepartamentos, name="Test_ShowDepartamentos"),
    #path('Test_ShowEmpleados/', Test_ShowEmpleados, name="Test_ShowEmpleados"),
]