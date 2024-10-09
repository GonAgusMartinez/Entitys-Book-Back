from django.urls import path
from .views import SupervivienteList, SupervivienteDetail

urlpatterns = [
    path('supervivientes/', SupervivienteList.as_view(), name='supervivientes-list'),
    path('supervivientes/<int:pk>/', SupervivienteDetail.as_view(), name='supervivientes-detail'),
]