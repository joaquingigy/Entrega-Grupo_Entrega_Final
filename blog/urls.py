from unicodedata import name 
from django.urls import path 
from .views import Blogs, Blog, Equipos, Equipo, login_request, registro

urlpatterns = [
    path('', Blogs.as_view() , name='blogs') ,
    path('blog/<pk>', Blog.as_view() , name="blog") ,
    path('equipos/', Equipos.as_view() , name='equipos') ,
    path('equipo/<pk>', Equipo.as_view() , name='equipo') ,
    path('login/', login_request , name='login') ,
    path('registro/', registro , name='registro'), 
    
]
