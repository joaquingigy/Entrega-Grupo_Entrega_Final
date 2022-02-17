from django.shortcuts import render
from .models import Blog, Equipo
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

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
    
def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario , password=clave)
            
            if user is not None:
                login(request, user)
                
                return render(request, 'blog/inicio.html', {'mensaje' : f'Bienvenido {usuario}'})
            
            else:
                
                return render(request, 'blog/inicio.html', {'mensaje' : 'Los datos ingresados no corresponden a ningún usuario'})
            
        else:
            
            return render(request, 'blog/inicio.html', {'mensaje' : 'Los datos ingresados no son válidos'})

    form = AuthenticationForm()
    
    return render(request, 'blog/login.html' , {'form' : form})