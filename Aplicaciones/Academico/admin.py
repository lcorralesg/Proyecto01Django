from django.contrib import admin

# Register your models here.
from .models import Curso, Especialidad, Docente

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'creditos', 'especialidad', 'docente')
    
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('idEspecialidad', 'nombre', 'descripcion')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('idDocente', 'apellido', 'nombre', 'fingreso', 'dni', 'telefono')