from django.urls import path, include
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('agregar_hora',agregar_hora, name='agregar_hora'),
]