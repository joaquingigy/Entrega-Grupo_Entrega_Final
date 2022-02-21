from unicodedata import name
from xml.etree.ElementInclude import include
from django import views 
from django.urls import path 

from .views import Blogs, Blog, Equipos, Equipo, buscar, busqueda_equipo, equipos_formulario, director_tecnico_add, director_tecnico_delete, director_tecnico_update, DirectorTecnico, jugador_update, jugador_delete, jugador_add, Jugador, equipo_add, equipo_delete, equipo_update, login_request, registro, editarPerfil,blog_add,DirectoresTecnicos,Jugadores


urlpatterns = [
    path('', Blogs.as_view() , name='blogs') ,
    path('blog/add', blog_add , name='blog_add'),
    path('blog/<pk>', Blog.as_view() , name="blog") ,
    path('equipos/', Equipos.as_view() , name='equipos') ,
    path('equipo/<pk>', Equipo.as_view() , name='equipo') ,
    path('equiposFormulario', equipos_formulario, name='equipos_formulario'),
    path('busquedaEquipo', busqueda_equipo, name='busqueda_equipo'),
    path('buscar', buscar, name='buscar'),
    path('login/', login_request , name='login') ,
    path('registro/', registro , name='registro'), 
    path('editarperfil',editarPerfil , name = "Editar Perfil" ), 

    path('jugadores', Jugadores.as_view(), name='jugadores'),
    path('jugador/add', jugador_add, name='jugador_add'),
    path('jugador/delete/<id_jugador>', jugador_delete, name='jugador_delete'),
    path('jugador/update/<id_jugador>', jugador_update, name='jugador_update'),
    # path('equipos', equipos, name='equipos'),
    path('equipo/add', equipo_add, name='equipo_add'),
    path('equipo/delete/<id_equipo>', equipo_delete, name='equipo_delete'),
    path('equipo/update/<id_equipo>', equipo_update, name='equipo_update'),
    path('directores_tecnicos', DirectoresTecnicos.as_view(), name='directores_tecnicos'),
    path('director_tecnico/add', director_tecnico_add, name='director_tecnico_add'),
    path('director_tecnico/delete/<id_director_tecnico>', director_tecnico_delete, name='director_tecnico_delete'),
    path('director_tecnico/update/', director_tecnico_update, name='director_tecnico_update'),
    path('director_tecnico/<pk>', DirectorTecnico.as_view(), name='director_tecnico'),
    path('jugador/<pk>', Jugador.as_view(), name='jugador'),
    
]


