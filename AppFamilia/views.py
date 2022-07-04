from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

def inicio(request):
    return render(request, 'AppFamilia/inicio.html')

def crearPersona(request):
    persona1=Persona(nombre="Miguel Angel", edad=62, nacimiento="1960-4-22")
    persona1.save()
    texto=f"Se creo una persona con nombre {persona1.nombre}, que tiene {persona1.edad} y nació el día {persona1.nacimiento}."
    
    persona2=Persona(nombre="Patricia", edad=59, nacimiento="1963-4-26")
    persona2.save()
    texto2=f"Se creo una persona con nombre {persona2.nombre}, que tiene {persona2.edad} y nació el día {persona2.nacimiento}."
    
    persona3=Persona(nombre="Andrés", edad=31, nacimiento="1991-10-19")
    persona3.save()
    texto3=f"Se creo una persona con nombre {persona3.nombre}, que tiene {persona3.edad} y nació el día {persona3.nacimiento}."

    return HttpResponse(texto+texto2+texto3)