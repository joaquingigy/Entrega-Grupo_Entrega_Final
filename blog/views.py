from django.shortcuts import render
from .models import Blog, Equipo
from django.views.generic import ListView, DetailView

# Create your views here.
class Blogs(ListView):
    model = Blog
    template_name = 'blog/inicio.html'
    
class Blog(DetailView):
    model = Blog
    template_name = 'blog/blog.html'
    
class Equipos(ListView):
    model = Equipo
    template_name = 'blog/equipos.html'
    
class Equipo(DetailView):
    model = Equipo
    template_name = 'blog/equipo.html'
    
    