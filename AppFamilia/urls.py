from django.contrib import admin
from django.urls import path
from .views import crearPersona, inicio

urlpatterns = [
    path('',inicio),
    path('crearpersona/', crearPersona),
]
