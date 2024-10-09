from django.urls import path
from .views import AsesinoList, AsesinoDetail

urlpatterns = [
    path('asesinos/', AsesinoList.as_view(), name='asesinos-list'),
    path('asesinos/<int:pk>/', AsesinoDetail.as_view(), name='asesinos-detail'),
]
