from django.contrib import admin
from .models import Usuario, Inscripcion
from .forms import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources 
# Register your models here.

class UsuarioResource(resources.ModelResource):
    class Meta:
        model = Usuario

class UsuarioAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = UsuarioResource
    actions = ["activacion_logica_Usuario"]
    search_fields = ["nombre"]
    form = FormRegistro


def activacion_logica_Usuario(self, request, queryset):
    for autor in queryset:
        autor.estado = False
        autor.save()

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Inscripcion)

