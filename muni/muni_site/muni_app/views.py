from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import ingresar_hora
from django.contrib import messages
# Create your views here.
def home(request):
    horas = hora.objects.all()
    dias = agenda_semanal.objects.all()
    data = {
        'horas':horas,
        'dias':dias
    }
    return render(request,"muni_app/home.html",data)

def agregar_hora(request):
    formulario = ingresar_hora()
    data = {
        'form':formulario
    }
    if request.method == 'POST':
        formulario = ingresar_hora(data=request.POST or None)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "hora ingresada correctamente!")
            return redirect(to="home")
    return render(request, "muni_app/CRUD/agregar_hora.html",data)