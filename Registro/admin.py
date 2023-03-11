from django.contrib import admin
from Registro.models import *
from django.contrib import admin
from .models import Usuario
from .forms import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources 
# Register your models here.

class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario

class UsuarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = UsuarioResource
    display = ["activacion_logica_Usuario"]
    search_fields = ["nombre"]
    form = FormRegistro


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Usuario)
