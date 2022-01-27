from unicodedata import name 
from django.urls import path 
from AppModels.views import buscar, busqueda_copas_ganadas, busqueda_copas_ganadas, crear_equipo, director_tecnico, equipo, jugador, inicio,equipos_formulario, jugadores_formulario, directores_tecnicos_formulario

urlpatterns = [
    path('equipo/<nombre>/<copas_ganadas>', crear_equipo),
    path('', inicio, name ='inicio'),
    path('equipo', equipo , name ='equipo'),  
    path('jugador', jugador, name ='jugador'), 
    path('director_tecnico', director_tecnico, name ='director_tecnico'), 
    path('equiposFormulario', equipos_formulario, name = 'equipos_formulario'),
    path('jugadoresFormulario', jugadores_formulario, name = 'jugadores_formulario'), 
    path('director_tecnicoFormulario', directores_tecnicos_formulario, name = 'directores_tecnicos_formularios'),
    path('busqueda_copas_ganadas', busqueda_copas_ganadas, name='busqueda_equipo'),
    path('buscar', buscar, name='buscar'),
]

