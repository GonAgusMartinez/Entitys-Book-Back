from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Modelos.urls_asesinos')),        
    path('api/', include('Modelos.urls_habilidadesase')),  
    path('api/', include('Modelos.urls_supervivientes')),  
    path('api/', include('Modelos.urls_habilidadessup')),  
]