from unicodedata import name
from django.urls import path 
from AppModels.views import crear_equipo, director_tecnico, equipo, jugador, inicio 

urlpatterns = [
    path('equipo/<nombre>/<copas_ganadas>', crear_equipo),
    path('', inicio, name='inicio'),
    path('equipo', equipo , name='equipo'),  
    path('jugador', jugador,name='jugador'), 
    path('director_tecnico', director_tecnico,name='director_tecnico'), 
]