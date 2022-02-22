import re
from django.shortcuts import redirect, render

from django.views.generic import ListView, DetailView
from django.contrib.auth import login, authenticate
from .forms import AvatarFormulario, UserRegisterForm , UsereditForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from mailbox import NoSuchMailboxError
from django.forms import model_to_dict
from django.http import HttpResponse

# from blog.views import director_tecnico, equipo, equipos_formulario, jugador
from blog.models import Blog, DirectorTecnico, Equipo, Jugador, Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .forms import UserRegisterForm, EquipoForm, JugadorForm, DirectorTecnicoForm,BlogForm

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
        
    
class BlogView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'
    
class Equipos(ListView):
    model = Equipo
    template_name = 'blog/equipos.html'
    
class EquipoView(DetailView):
    model = Equipo
    template_name = 'blog/equipo.html'
    
class Jugadores(ListView):
    model = Jugador
    template_name = 'blog/jugadores.html'
    
class JugadorView(DetailView):
    model = Jugador
    template_name = 'blog/jugador.html'    
    
class DirectoresTecnicos (ListView):
    model = DirectorTecnico
    template_name = 'blog/directores_tecnicos.html'
    
class DirectorTecnicoView (DetailView):
    model = DirectorTecnico
    template_name = 'blog/director_tecnico.html'   


def equipos_formulario(request):
    if request.method == 'POST':
        formulario = EquipoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Equipo.objects.create(nombre=data['equipo'], pais=data['pais'], liga=data['liga'], copasGanadas=data['copasGanadas'])
            return redirect('equipos')
        else:
            formulario = EquipoForm()
        return render(request, 'blog/equiposFormulario.html')

def busqueda_equipo(request):
    return render(request, 'blog/busquedaEquipo.html')

def buscar(request):
    copasGanadas = request.GET.get("copasGanadas")
    
    if copasGanadas:
        equipo = Equipo.objects.filter(copasGanadas=copasGanadas)

        return render(request, 'blog/buscar.html', 
            {'equipos': equipo, 'copasGanadas': copasGanadas})
    else:
        return HttpResponse('No se envio un numero de copas ganadas valido.')


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

   
def equipos_formulario(request):
    pass

#Hecho con clases

# def equipos(request):
#     return render(request,
#         'blog/equipos.html',
#         {'equipos': Equipo.objects.all() }
#         )

# def jugador(request):
#     return render(request,
#         'blog/jugador.html',
#         {'jugador': Jugador.objects.all() }
#         )

# def director_tecnico(request):
#     return render(request,
#         'blog/director_tecnico.html',
#         {'director_tecnico': DirectorTecnico.objects.all() }
#         )

def equipo_add(request):
    if request.method == 'POST':
        formulario = EquipoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Equipo.objects.create(
                nombre=data['nombre'],
                pais=data['pais'],
                liga=data['liga'],
                copasGanadas=data['copasGanadas']
                )
            return redirect('equipos')
    else:
        formulario = EquipoForm()
    return render(request, 'blog/equiposFormulario.html', {'formulario': formulario})

def jugador_add(request):
    if request.method == 'POST':
        formulario = JugadorForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Jugador.objects.create(
                nombre=data['nombre'],
                apellido=data['apellido'],
                copasGanadas=data['copasGanadas'],
                equipo=data['equipo'],
                goles=data['goles'],
                )
            return redirect('jugadores')
    else:
        formulario = JugadorForm()
    return render(request, 'blog/equiposFormulario.html', {'formulario': formulario})

def director_tecnico_add(request):
    if request.method == 'POST':
        formulario =DirectorTecnicoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            DirectorTecnico.objects.create(
                nombre=data['nombre'],
                apellido=data['apellido'],
                copasGanadas=data['copasGanadas'],
                equipo=data['equipo'],
                aniosExperiencia=data['aniosExperiencia'],
                )
            return redirect('directores_tecnicos')
    else:
        formulario = DirectorTecnicoForm()
    return render(request, 'blog/equiposFormulario.html', {'formulario': formulario})

def equipo_delete(request, id_equipo):
    equipo = Equipo.objects.get(id=id_equipo) 
    equipo.delete()

    return redirect('equipos')

def jugador_delete(request, id_jugador):
    jugador = Jugador.objects.get(id=id_jugador) 
    jugador.delete()

    return redirect('jugadores')

def director_tecnico_delete(request, id_director_tecnico):
    director_tecnico = DirectorTecnico.objects.get(id=id_director_tecnico) 
    director_tecnico.delete()

    return redirect('directores_tecnicos')

def equipo_update(request, id_equipo):
    equipo = Equipo.objects.get(id=id_equipo) 

    if request.method == 'POST':
        formulario = EquipoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
          
            equipo.nombre = data['nombre']
            equipo.pais=data['pais']
            equipo.liga=data['liga']
            equipo.copasGanadas=data['copasGanadas']

            equipo.save()  
            
            return redirect('equipos')
    else:
        formulario = EquipoForm(model_to_dict(equipo))
    return render(request, 'blog/equiposFormulario.html', {'formulario': formulario})

def jugador_update(request, id_jugador):
    jugador = Jugador.objects.get(id=id_jugador) 

    if request.method == 'POST':
        formulario = JugadorForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
          
            jugador.nombre = data['nombre']
            jugador.apellido=data['apellido']
            jugador.equipo=data['equipo']
            jugador.copasGanadas=data['copasGanadas']
            jugador.goles=data['goles']
            jugador.save()  
            
            return redirect('jugadores')
    else:
        formulario = JugadorForm(model_to_dict(jugador))
    return render(request, 'blog/equiposFormulario.html', {'formulario': formulario})

def director_tecnico_update(request, id_director_tecnico):
    director_tecnico = DirectorTecnico.objects.get(id=id_director_tecnico) 

    if request.method == 'POST':
        formulario = DirectorTecnicoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
          
            director_tecnico.nombre = data['nombre']
            director_tecnico.apellido=data['apellido']
            director_tecnico.equipo=data['equipo']
            director_tecnico.copasGanadas=data['copasGanadas']
            director_tecnico.aniosExperiencia=data ['aniosExperiencia']
            director_tecnico.save()  
            
            return redirect('directores_tecnicos')
    else:
        formulario = DirectorTecnicoForm(model_to_dict(director_tecnico))
    return render(request, 'blog/equiposFormulario.html', {'formulario': formulario})

def blog_add(request):
    if request.method == 'POST':
        formulario = BlogForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Blog.objects.create(
                titulo=data['titulo'],
                cuerpo=data['cuerpo'],
                autor=data['autor'],
            
                )
            return redirect('blogs')
    else:
        formulario = BlogForm()
    return render(request, 'blog/equiposFormulario.html', {'formulario': formulario})

def blog_update(request, id_blog):
    blog = Blog.objects.get(id=id_blog) 

    if request.method == 'POST':
        formulario = BlogForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
          
            blog.titulo = data['titulo']
            blog.cuerpo=data['cuerpo']
            blog.autor=data['autor']
            

            blog.save()  
            
            return redirect('blogs')
    else:
        formulario = BlogForm(model_to_dict(blog))
    return render(request, 'blog/equiposFormulario.html', {'formulario': formulario})

def blog_delete(request, id_blog):
    blog = Blog.objects.get(id=id_blog) 
    blog.delete()

    return redirect('blogs')