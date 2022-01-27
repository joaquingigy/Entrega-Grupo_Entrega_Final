from unicodedata import name 
from django.urls import path 

from AppModels.views import buscar, busqueda_copas_ganadas, crear_equipo, director_tecnico, equipo, jugador, inicio,equipos_formulario,director_tecnico_formulario, jugador_formulario

urlpatterns = [
    path('equipo/<nombre>/<copas_ganadas>', crear_equipo),
    path('', inicio, name='inicio'),
    path('equipo', equipo , name='equipo'),  
    path('jugador', jugador,name='jugador'), 
    path('director_tecnico', director_tecnico,name='director_tecnico'), 
    path('equiposFormulario',equipos_formulario, name= 'equipos_formulario'),
    path('directorTecnicoFormulario',director_tecnico_formulario,name= 'director_tecnico_formulario'),
    path('jugadorFormulario',jugador_formulario, name='jugador_formulario'),
    path('busquedaCopasGanadas',busqueda_copas_ganadas,name='busqueda_copas_ganadas'),
    path('buscar',buscar, name='buscar'),
]
