from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('mantenimiento/', include('administration.urls')),
    path('', include('ventas.urls')),
    path('rally/', include('rally.urls')),
]
