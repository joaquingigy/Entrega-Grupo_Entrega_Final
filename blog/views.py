import re
from django.shortcuts import redirect, render

from django.views.generic import ListView, DetailView
from django.contrib.auth import login, authenticate
from .forms import AvatarFormulario, UserEditForm, UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

from mailbox import NoSuchMailboxError
from django.forms import model_to_dict
from django.http import HttpResponse

# from blog.views import director_tecnico, equipo, equipos_formulario, jugador
from blog.models import Blog, DirectorTecnico, Equipo, Jugador, Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .forms import UserRegisterForm, EquipoForm, JugadorForm, DirectorTecnicoForm,BlogForm

from django.contrib.auth.models import User
# Create your views here.
class Blogs(ListView):
     
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)     
    
        avatares=Avatar.objects.filter(user = self.request.user.id)
        if avatares.__len__():        
            context["url"] = avatares[0].imagen.url 
        return context
    
    model = Blog
    template_name = 'blog/inicio.html'
    
    
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
    if not request.user.is_authenticated: 
        if request.method == "POST":
            form = AuthenticationForm(request, data= request.POST)
            
            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                clave = form.cleaned_data.get('password')
                
                user = authenticate(username=usuario , password=clave)
                
                if user is not None:
                    login(request, user)
                    
                    return redirect ('blogs')                                                  #(request, 'blog/inicio.html', {'mensaje' : f'Bienvenido {usuario}'})
                
                else:
                    #request.method = "GET" 
                    return render(request, 'blog/login.html', {'mensaje' : 'Los datos ingresados no corresponden a ningún usuario','form':form})
                
            else:
                
                #request.method = "GET"
                return render(request, 'blog/login.html', {'mensaje' : 'Los datos ingresados no son válidos','form':form })

        form = AuthenticationForm()
        
        return render(request, 'blog/login.html' , {'form' : form})
    else: 
        return render (request,'blog/login.html',{'mensaje' : 'Ya estás logueado'} )


def registro (request):
    if request.method == 'POST' :
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)    
        if form.is_valid():
            username = form.cleaned_data ['username']
            form.save()
            return redirect ('login')  #(request, "blog/inicio.html", {"mensaje": "Usuario Creado :)"})     
        
    else:
         # form = UserCreationForm()
        form = UserRegisterForm()
            
    return render (request, 'blog/registro.html', {'form':form})

@login_required
def editarPerfil(request):
    #Instancia del login
    
    #Si es método POST hago lo mismo que el agregar 
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm (request.POST)
        if miFormulario.is_valid (): #Si pasó la validación de Django
            
            informacion = miFormulario.cleaned_data
            
            #Datos que se modificarán
            usuario.email = informacion ['email']
            usuario.password1 = informacion ['password1']
            usuario.password2 = informacion ['password1']
            usuario.last_name = informacion ['last_name']
            usuario.first_name =  informacion ['first_name']
            usuario.save ()
            
            return redirect ('blogs') #(request, "blog/inicio.html") #Vuelvo al inicio o a donde quieran
        else:   
            return redirect ('editar_perfil')
    #En caso que no sea post
    else:
        #Creo el formulario con los datos que voy a modificar
        miFormulario = UserEditForm (initial = { 'email': usuario.email,'last_name':usuario.last_name,'first_name':usuario.first_name})
        
        #Voy al html que me permite editar
        return render (request, "blog/editar_perfil.html", {"miFormulario":miFormulario , "usuario":usuario})

@login_required
def agregar_avatar (request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario (request.POST , request.FILES)
        
        if miFormulario.is_valid():
            avatar = Avatar (user = request.user , imagen = miFormulario.cleaned_data ['imagen'] )    
            avatar.save ()
            return redirect ('blogs')
    else:
        miFormulario = AvatarFormulario ()
    
    return render (request,'blog/crear_avatar.html' , {'miFormulario': miFormulario} )

   
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
                subtitulo = data['subtitulo'],
                cuerpo=data['cuerpo'],
                autor=data['autor'],
                imagen= data['imagen'],
            
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
            blog.subtitulo = data['subtitulo']
            blog.cuerpo=data['cuerpo']
            blog.autor=data['autor']
            blog.imagen= data['imagen']

            blog.save()  
            
            return redirect('blogs')
    else:
        formulario = BlogForm(model_to_dict(blog))
    return render(request, 'blog/equiposFormulario.html', {'formulario': formulario})

def blog_delete(request, id_blog):
    blog = Blog.objects.get(id=id_blog) 
    blog.delete()

    return redirect('blogs')

# class UserView (DetailView):
#     model = User
#     template_name = 'blog/perfil.html'
#     context_object_name = 'user_object'
#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)     
    
#         avatares=Avatar.objects.filter(user = self.request.user.id)
#         if avatares.__len__():        
#             context["url"] = avatares[0].imagen.url 
#         return context
def user_view (request):
    if request.user.is_authenticated:
        avatares=Avatar.objects.filter(user = request.user.id)
        if avatares.__len__():        
            url = avatares[0].imagen.url 
        else:
            url = ""
        return render (request,'blog/perfil.html',{'url': url})

def about_view (request):
    return render (request,"blog/about.html")

def error404_view (request):
    return render (request,"blog/error404.html")