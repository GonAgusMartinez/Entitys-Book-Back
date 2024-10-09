from django.contrib import admin
from django.urls import path
from Modelosyrutas.views import AsesinoList, AsesinoDetail, SupervivienteList, SupervivienteDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/asesinos/', AsesinoList.as_view(), name='asesinos-list'),
    path('api/asesinos/<int:pk>/', AsesinoDetail.as_view(), name='asesinos-detail'),
    path('api/supervivientes/', SupervivienteList.as_view(), name='supervivientes-list'),
    path('api/supervivientes/<int:pk>/', SupervivienteDetail.as_view(), name='supervivientes-detail'),
]