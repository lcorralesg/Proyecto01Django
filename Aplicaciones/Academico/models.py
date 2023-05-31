from django.db import models

# Create your models here.

class Especialidad(models.Model):
    idEspecialidad = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    
class Docente(models.Model):
    idDocente = models.CharField(primary_key=True, max_length=6)
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    fingreso = models.DateField()
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return self.apellido + ' ' + self.nombre
    
class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveIntegerField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    