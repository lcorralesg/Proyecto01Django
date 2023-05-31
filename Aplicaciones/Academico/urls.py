from django.urls import path
from .import views

urlpatterns = [
    path('', views.home),
    path('registrarcurso', views.registrarcurso),
    path('eliminarcurso/<codigo>', views.eliminarcurso),
]