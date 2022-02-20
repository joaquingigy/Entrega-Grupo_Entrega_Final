from unicodedata import name 
from django.urls import path 
from .views import Blogs, Blog, Equipos, Equipo, buscar, busqueda_equipo, equipos_formulario, director_tecnico_add, director_tecnico_delete, director_tecnico_update, director_tecnico, jugador_update, jugador_delete, jugador_add, jugador, equipos, equipo_add, equipo_delete, equipo_update, login_request, registro

urlpatterns = [
    path('', Blogs.as_view() , name='blogs') ,
    path('blog/<pk>', Blog.as_view() , name="blog") ,
    path('equipos/', Equipos.as_view() , name='equipos') ,
    path('equipo/<pk>', Equipo.as_view() , name='equipo') ,
    path('equiposFormulario', equipos_formulario, name='equipos_formulario'),
    path('busquedaEquipo', busqueda_equipo, name='busqueda_equipo'),
    path('buscar', buscar, name='buscar'),
    path('login/', login_request , name='login') ,
    path('registro/', registro , name='registro'), 
    path('jugador', jugador, name='jugadores'),
    path('jugador/add', jugador_add, name='jugador_add'),
    path('jugador/delete/<id_jugador>', jugador_delete, name='jugador_delete'),
    path('jugador/update/<id_jugador>', jugador_update, name='jugador_update'),
    path('equipos', equipos, name='equipos'),
    path('equipo/add', equipo_add, name='equipo_add'),
    path('equipo/delete/<id_equipo>', equipo_delete, name='equipo_delete'),
    path('equipo/update/<id_equipo>', equipo_update, name='equipo_update'),
    path('director_tecnico', director_tecnico, name='director_tecnico'),
    path('director_tecnico/add', director_tecnico_add, name='director_tecnico_add'),
    path('director_tecnico/delete/<id_director_tecnico>', director_tecnico_delete, name='director_tecnico_delete'),
    path('director_tecnico/update/', director_tecnico_update, name='director_tecnico_update')
]
