from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.utils.translation import gettext_lazy as _
from .models import Curso, Especialidad, Docente

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'El nombre de usuario debe ser menor a 150 caracteres y no puede contener caracteres especiales'
        self.fields['password1'].help_text = 'La contraseña debe tener al menos 3 caracteres'
        self.fields['password2'].help_text = 'La contraseña debe tener al menos 3 caracteres'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Academico:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'autenticacion/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'autenticacion/login.html', {'form': form})

@login_required(login_url='Academico:login')
def home (request):
    cursosListado = Curso.objects.all()
    especialidadesListado = Especialidad.objects.all()
    docentesListado = Docente.objects.all()
    context = {'cursos': cursosListado, 'especialidades': especialidadesListado, 'docentes': docentesListado}
    return render(request, 'GestionCursos.html', context)

@login_required(login_url='Academico:login')
def registrarcurso (request):
    codigo = request.POST['txtcodigo']
    nombre = request.POST['txtnombre']
    creditos = request.POST['numCreditos']
    especialidad_seleccionada = request.POST['seEspecialidad']
    docente_seleccionado = request.POST['seDocente']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, especialidad=Especialidad.objects.get(idEspecialidad=especialidad_seleccionada), docente=Docente.objects.get(idDocente=docente_seleccionado))
    return redirect('/')

@login_required(login_url='Academico:login')
def eliminarcurso (request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')

@login_required(login_url='Academico:login')
def editarcurso (request, codigo):
    cursoselec = Curso.objects.get(codigo=codigo)
    especialidadesListado = Especialidad.objects.all()
    docentesListado = Docente.objects.all()
    cursosListado = Curso.objects.all()
    context = {'cursoselec': cursoselec, 'especialidades': especialidadesListado, 'docentes': docentesListado, 'cursos': cursosListado}
    return render(request, 'EditarCurso.html', context)

@login_required(login_url='Academico:login')
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

@login_required(login_url='Academico:login')
def docentes (request):
    docentesListado = Docente.objects.all()
    context = {'docentes': docentesListado}
    return render(request, 'GestionDocentes.html', context)

@login_required(login_url='Academico:login')
def registrardocente (request):
    idDocente = request.POST['txtidDocente']
    apellido = request.POST['txtapellido']
    nombre = request.POST['txtnombre']
    fingreso = request.POST['txtfingreso']
    dni = request.POST['txtdni']
    telefono = request.POST['txttelefono']

    docente = Docente.objects.create(idDocente=idDocente, apellido=apellido, nombre=nombre, fingreso=fingreso, dni=dni, telefono=telefono)

    return redirect('/docentes')

@login_required(login_url='Academico:login')
def eliminardocente (request, idDocente):
    docente = Docente.objects.get(idDocente=idDocente)
    docente.delete()
    return redirect('/docentes')

@login_required(login_url='Academico:login')
def editardocente (request, idDocente):
    docenteselec = Docente.objects.get(idDocente=idDocente)
    docentesListado = Docente.objects.all()
    context = {'docenteselec': docenteselec, 'docentes': docentesListado}
    return render(request, 'EditarDocente.html', context)

@login_required(login_url='Academico:login')
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

@login_required(login_url='Academico:login')
def especialidades (request):
    especialidadesListado = Especialidad.objects.all()
    context = {'especialidades': especialidadesListado}
    return render(request, 'GestionEspecialidades.html', context)

@login_required(login_url='Academico:login')
def registrarespecialidad (request):
    idEspecialidad = request.POST['txtidEspecialidad']
    nombre = request.POST['txtnombre']
    descripcion = request.POST['txtdescripcion']

    especialidad = Especialidad.objects.create(idEspecialidad=idEspecialidad, nombre=nombre, descripcion=descripcion)

    return redirect('/especialidades')

@login_required(login_url='Academico:login')
def eliminarespecialidad (request, idEspecialidad):
    especialidad = Especialidad.objects.get(idEspecialidad=idEspecialidad)
    especialidad.delete()
    return redirect('/especialidades')

@login_required(login_url='Academico:login')
def editarespecialidad (request, idEspecialidad):
    especialidadselec = Especialidad.objects.get(idEspecialidad=idEspecialidad)
    especialidadesListado = Especialidad.objects.all()
    context = {'especialidadselec': especialidadselec, 'especialidades': especialidadesListado}
    return render(request, 'EditarEspecialidad.html', context)

@login_required(login_url='Academico:login')
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
@login_required(login_url='Academico:login')
def listacursos (request):
    cursosListado = Curso.objects.all()
    context = {'cursos': cursosListado}
    return render(request, 'ListaCursos.html', context)

@login_required(login_url='Academico:login')
def listadocentes (request):
    docentesListado = Docente.objects.all()
    context = {'docentes': docentesListado}
    return render(request, 'ListaDocentes.html', context)

@login_required(login_url='Academico:login')
def listaespecialidades (request):
    especialidadesListado = Especialidad.objects.all()
    context = {'especialidades': especialidadesListado}
    return render(request, 'ListaEspecialidades.html', context)

@login_required(login_url='Academico:login')
def buscarcurso (request):
    nombre = request.POST['cursobuscado']
    cursosListado = Curso.objects.filter(nombre__startswith=nombre)
    context = {'cursos': cursosListado}
    return render(request, 'ListaCursos.html', context)

@login_required(login_url='Academico:login')
def buscardocente (request):
    apellido = request.POST['docentebuscado']
    fingreso = request.POST['docentebuscadofecha']
    if apellido != '':
        docentesListado = Docente.objects.filter(apellido=apellido)
    else:
        docentesListado = Docente.objects.filter(fingreso=fingreso)
    context = {'docentes': docentesListado}
    return render(request, 'ListaDocentes.html', context)

@login_required(login_url='Academico:login')
def buscarespecialidad (request):
    nombre = request.POST['especialidadbuscada']
    especialidadesListado = Especialidad.objects.filter(nombre=nombre)
    context = {'especialidades': especialidadesListado}
    return render(request, 'ListaEspecialidades.html', context)