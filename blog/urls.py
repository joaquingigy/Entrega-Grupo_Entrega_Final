from unicodedata import name
from xml.etree.ElementInclude import include
from django import views 
from django.urls import path 

from .views import Blogs, BlogView, Equipos, EquipoView, agregar_avatar, buscar, busqueda_equipo, equipos_formulario, director_tecnico_add, director_tecnico_delete, director_tecnico_update, DirectorTecnicoView, jugador_update, jugador_delete, jugador_add, JugadorView, equipo_add, equipo_delete, equipo_update, login_request, registro, editarPerfil,blog_add,DirectoresTecnicos,Jugadores,blog_update,blog_delete

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', Blogs.as_view() , name='blogs') ,
    path('blog/add', blog_add , name='blog_add'),
    path('equipos/', Equipos.as_view() , name='equipos') ,
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
    path('director_tecnico/update/<id_director_tecnico>', director_tecnico_update, name='director_tecnico_update'),
    path('blog/update/<id_blog>', blog_update, name='blog_update'),
    path('blog/delete/<id_blog>', blog_delete, name='blog_delete'),
    path('blog/<pk>', BlogView.as_view() , name="blog") ,
    path('equipo/<pk>', EquipoView.as_view() , name='equipo') ,
    path('director_tecnico/<pk>', DirectorTecnicoView.as_view(), name='director_tecnico'),
    path('jugador/<pk>', JugadorView.as_view(), name='jugador'),
    path('agregarAvatar', agregar_avatar, name ="AgregarAvatar"),
    path('logout',LogoutView.as_view (template_name = 'blog/logout.html'), name = 'logout'),
]


