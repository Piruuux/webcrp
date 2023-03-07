from django.shortcuts import render
from Registro.forms import *
from Registro.models import *
from django.views.generic import *
from django.http import HttpResponse

# Create your views here.
class Usuario_Inscripsion(CreateView):
    model = Usuario
    success_url = 'completado/'
    fields = ['nombre', 'apellido', 'email', 'genero', 'fecha_de_nacimiento', 'pais', 'estado', 'dni', 'telefono', 'grupo_de_running', 'talle_de_remera', 'categoria']
    template_name = 'Registro/registro.html'


def Completado(request):
    return render (request, 'Registro/completado.html')


def Ususario(request):
    data = {
        "form": Usuario()

    }

    if request.method == "POST":
        formulario = Usuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario
    


    return render(request, "Registro/registro.html", data)