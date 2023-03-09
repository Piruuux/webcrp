from django.shortcuts import render, redirect 
from .forms import *
from Registro.models import *
from django.views.generic import *
from django.contrib.auth import *


# Create your views here.
class Usuario_Inscripsion(CreateView):
    model = Usuario
    success_url = 'completado/'
    fields = ['nombre', 'apellido', 'email', 'genero', 'fecha_de_nacimiento', 'pais', 'estado', 'dni', 'telefono', 'grupo_de_running', 'talle_de_remera', 'categoria']
    template_name = 'Registro/registro.html'

def Completado(request):
    return render (request, 'Registro/completado.html')




def guardar_formulario(request):
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            # Guardamos los datos del formulario en la base de datos
            Usuario = form.save()
            Usuario.save()
            return render(request, 'completado.html') # Redirigimos a una página de éxito
    #else:
        #form = FormRegistron()
    #return render(request, 'Registro.html', {'form': form})s   