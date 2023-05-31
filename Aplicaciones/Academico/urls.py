from django.urls import path
from .import views

app_name = 'Academico'

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('', views.home, name='home'),
    path('registrarcurso', views.registrarcurso , name='registrarcurso'),
    path('eliminarcurso/<codigo>', views.eliminarcurso , name='eliminarcurso'),
    path('editarcurso/<codigo>', views.editarcurso, name='editarcurso'),
    path('actualizarcurso', views.actualizarcurso, name='actualizarcurso'),
    path('docentes', views.docentes, name='docentes'),
    path('registrardocente', views.registrardocente, name='registrardocente'),
    path('eliminardocente/<idDocente>', views.eliminardocente, name='eliminardocente'),
    path('editardocente/<idDocente>', views.editardocente, name='editardocente'),
    path('actualizardocente', views.actualizardocente, name='actualizardocente'),
    path('especialidades', views.especialidades, name='especialidades'),
    path('registrarespecialidad', views.registrarespecialidad, name='registrarespecialidad'),
    path('eliminarespecialidad/<idEspecialidad>', views.eliminarespecialidad, name='eliminarespecialidad'),
    path('editarespecialidad/<idEspecialidad>', views.editarespecialidad, name='editarespecialidad'),
    path('actualizarespecialidad', views.actualizarespecialidad, name='actualizarespecialidad'),
    path('listacursos', views.listacursos, name='listacursos'),
    path('buscarcurso', views.buscarcurso, name='buscarcurso'),
    path('listadocentes', views.listadocentes, name='listadocentes'),
    path('buscardocente', views.buscardocente, name='buscardocente'),
    path('listaespecialidades', views.listaespecialidades, name='listaespecialidades'),
    path('buscarespecialidad', views.buscarespecialidad, name='buscarespecialidad'),
]