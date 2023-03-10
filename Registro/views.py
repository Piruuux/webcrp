from django.shortcuts import render, redirect 
from .forms import *
from Registro.models import *
from django.views.generic import *
from django.contrib.auth import *

def guardar_formulario(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            Usuario = form.save()
            Usuario.save()
            return render(request, 'registro.html') 
    else:
        form = FormRegistron()
    return render(request, 'Registro/completado.html', {'form': form})




class Usuario_Inscripsion(CreateView):
    model = Usuario
    success_url = 'completado/'
    fields = ['nombre', 'apellido', 'email', 'genero', 'fecha_de_nacimiento', 'pais', 'estado', 'dni', 'telefono', 'grupo_de_running', 'talle_de_remera', 'categoria']
    template_name = 'Registro/registro.html'

def Completado(request):
    return render (request, 'Registro/completado.html')

