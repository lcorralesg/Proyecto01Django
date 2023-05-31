from django.shortcuts import render, redirect
from .models import Curso
# Create your views here.

def home (request):
    cursosListado = Curso.objects.all()
    return render(request, 'GestionCursos.html', {'cursos': cursosListado})

def registrarcurso (request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)

    return redirect('/')

def eliminarcurso (request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')