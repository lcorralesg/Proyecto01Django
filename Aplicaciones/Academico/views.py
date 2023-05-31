from django.shortcuts import render, redirect
from .models import Curso, Especialidad, Docente

def home (request):
    cursosListado = Curso.objects.all()
    especialidadesListado = Especialidad.objects.all()
    docentesListado = Docente.objects.all()
    context = {'cursos': cursosListado, 'especialidades': especialidadesListado, 'docentes': docentesListado}
    return render(request, 'GestionCursos.html', context)

def registrarcurso (request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['numCreditos']
    especialidad_seleccionada = request.POST['seEspecialidad']
    docente_seleccionado = request.POST['seDocente']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, especialidad=Especialidad.objects.get(idEspecialidad=especialidad_seleccionada), docente=Docente.objects.get(idDocente=docente_seleccionado))

    return redirect('/')

def eliminarcurso (request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

def editarcurso (request, codigo):
    cursoselec = Curso.objects.get(codigo=codigo)
    especialidadesListado = Especialidad.objects.all()
    docentesListado = Docente.objects.all()
    cursosListado = Curso.objects.all()
    context = {'cursoselec': cursoselec, 'especialidades': especialidadesListado, 'docentes': docentesListado, 'cursos': cursosListado}
    return render(request, 'EditarCurso.html', context)

def actualizarcurso (request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['numCreditos']
    especialidad_seleccionada = request.POST['seEspecialidad']
    docente_seleccionado = request.POST['seDocente']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.especialidad = Especialidad.objects.get(idEspecialidad=especialidad_seleccionada)
    curso.docente = Docente.objects.get(idDocente=docente_seleccionado)
    curso.save()

    return redirect('/')

def docentes (request):
    docentesListado = Docente.objects.all()
    context = {'docentes': docentesListado}
    return render(request, 'GestionDocentes.html', context)

def registrardocente (request):
    idDocente = request.POST['txtidDocente']
    apellido = request.POST['txtapellido']
    nombre = request.POST['txtnombre']
    fingreso = request.POST['txtfingreso']
    dni = request.POST['txtdni']
    telefono = request.POST['txttelefono']

    docente = Docente.objects.create(idDocente=idDocente, apellido=apellido, nombre=nombre, fingreso=fingreso, dni=dni, telefono=telefono)

    return redirect('/docentes')

def eliminardocente (request, idDocente):
    docente = Docente.objects.get(idDocente=idDocente)
    docente.delete()
    return redirect('/docentes')

def editardocente (request, idDocente):
    docenteselec = Docente.objects.get(idDocente=idDocente)
    docentesListado = Docente.objects.all()
    context = {'docenteselec': docenteselec, 'docentes': docentesListado}
    return render(request, 'EditarDocente.html', context)

def actualizardocente (request):
    idDocente = request.POST['txtidDocente']
    apellido = request.POST['txtapellido']
    nombre = request.POST['txtnombre']
    fingreso = request.POST['txtfingreso']
    dni = request.POST['txtdni']
    telefono = request.POST['txttelefono']

    docente = Docente.objects.get(idDocente=idDocente)
    docente.apellido = apellido
    docente.nombre = nombre
    docente.fingreso = fingreso
    docente.dni = dni
    docente.telefono = telefono
    docente.save()

    return redirect('/docentes')

def especialidades (request):
    especialidadesListado = Especialidad.objects.all()
    context = {'especialidades': especialidadesListado}
    return render(request, 'GestionEspecialidades.html', context)

def registrarespecialidad (request):
    idEspecialidad = request.POST['txtidEspecialidad']
    nombre = request.POST['txtnombre']
    descripcion = request.POST['txtdescripcion']

    especialidad = Especialidad.objects.create(idEspecialidad=idEspecialidad, nombre=nombre, descripcion=descripcion)

    return redirect('/especialidades')

def eliminarespecialidad (request, idEspecialidad):
    especialidad = Especialidad.objects.get(idEspecialidad=idEspecialidad)
    especialidad.delete()
    return redirect('/especialidades')

def editarespecialidad (request, idEspecialidad):
    especialidadselec = Especialidad.objects.get(idEspecialidad=idEspecialidad)
    especialidadesListado = Especialidad.objects.all()
    context = {'especialidadselec': especialidadselec, 'especialidades': especialidadesListado}
    return render(request, 'EditarEspecialidad.html', context)

def actualizarespecialidad (request):
    idEspecialidad = request.POST['txtidEspecialidad']
    nombre = request.POST['txtnombre']
    descripcion = request.POST['txtdescripcion']

    especialidad = Especialidad.objects.get(idEspecialidad=idEspecialidad)
    especialidad.nombre = nombre
    especialidad.descripcion = descripcion
    especialidad.save()

    return redirect('/especialidades')

# Listas de busqueda
def listacursos (request):
    cursosListado = Curso.objects.all()
    context = {'cursos': cursosListado}
    return render(request, 'ListaCursos.html', context)

def listadocentes (request):
    docentesListado = Docente.objects.all()
    context = {'docentes': docentesListado}
    return render(request, 'ListaDocentes.html', context)

def listaespecialidades (request):
    especialidadesListado = Especialidad.objects.all()
    context = {'especialidades': especialidadesListado}
    return render(request, 'ListaEspecialidades.html', context)

def buscarcurso (request):
    nombre = request.POST['cursobuscado']
    cursosListado = Curso.objects.filter(nombre__startswith=nombre)
    context = {'cursos': cursosListado}
    return render(request, 'ListaCursos.html', context)

def buscardocente (request):
    apellido = request.POST['docentebuscado']
    fingreso = request.POST['docentebuscadofecha']
    if apellido != '':
        docentesListado = Docente.objects.filter(apellido=apellido)
    else:
        docentesListado = Docente.objects.filter(fingreso=fingreso)
    context = {'docentes': docentesListado}
    return render(request, 'ListaDocentes.html', context)

def buscarespecialidad (request):
    nombre = request.POST['especialidadbuscada']
    especialidadesListado = Especialidad.objects.filter(nombre=nombre)
    context = {'especialidades': especialidadesListado}
    return render(request, 'ListaEspecialidades.html', context)

