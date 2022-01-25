from django.urls import path 
from AppModels.views import crear_equipo, director_tecnico, equipo, jugador, inicio 

urlpatterns = [
    path('equipo/<nombre>/<copas_ganadas>', crear_equipo),
    path('', inicio),
    path('equipo', equipo),  
    path('jugador', jugador), 
    path('director_tecnico', director_tecnico), 
]