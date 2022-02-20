import re
from django.shortcuts import redirect, render
from platformdirs import user_data_dir
from .models import Avatar, Blog, Equipo
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import AvatarFormulario, UserRegisterForm , UsereditForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required


# Create your views here.
class Blogs(ListView):
    # def __init__ (self):
    #     user = self.request.user.id
    #     avatares=Avatar.objects.filter(user)
    #     url = avatares [0].imagen.url
        
    model = Blog
    template_name = 'blog/inicio.html'
    
    # def get(self,request):
    #     user = self.request.user.id
    #     avatares=Avatar.objects.filter(user)
    #     self.url = avatares.imagen.url
        
    
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

def registro (request):
    if request.method == 'POST' :
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)    
        if form.is_valid():
            username = form.cleaned_data ['username']
            form.save()
            return render (request, "blog/login.html", {"mensaje": "Usuario Creado :)"})     
        
    else:
         # form = UserCreationForm()
        form = UserRegisterForm()
            
    return render (request, 'blog/registro.html', {'form':form})

def editarPerfil(request):
    #Instancia del login
    
    #Si es método POST hago lo mismo que el agregar 
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UsereditForm (request.POST)
        if miFormulario.is_valid (): #Si pasó la validación de Django
            
            informacion = miFormulario.cleaned_data
            
            #Datos que se modificarán
            usuario.email = informacion ['email']
            usuario.password1 = informacion ['password1']
            usuario.password2 = informacion ['password1']
            usuario.save ()
            
            return render (request, "blog/inicio.html") #Vuelvo al inicio o a donde quieran
    #En caso que no sea post
    else:
        #Creo el formulario con los datos que voy a modificar
        miFormulario = UsereditForm (initial = { 'email': usuario.email})
        
        #Voy al html que me permite editar
        return render (request, "blog/editarperfil.html", {"miFormulario":miFormulario , "usuario":usuario})

@login_required
def agregar_avatar (request):
    if request.method == 'POST':
        formulario = AvatarFormulario (request.Post , request. Files)
        
        if formulario.is_valid():
            avatar = Avatar (user = request.user , imagen = formulario.cleaned_data ['imagen'] )    
            avatar.save
            return redirect ('inicio')
    else:
        formulario = AvatarFormulario ()
    
    return render (request,'blog/crear_avatar.html' , {'form': formulario} )

   
