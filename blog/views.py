from mailbox import NoSuchMailboxError
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppModels.forms import EquipoFormulario

from AppModels.views import director_tecnico, equipo, equipos_formulario, jugador
from .models import Blog, DirectorTecnico, Equipo, Jugador
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate 
from .forms import UserRegisterForm, EquipoForm, JugadorForm, DirectorTecnicoForm

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

def equipos_formulario(request):
    if request.method == 'POST':
        formulario = EquipoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Equipo.objects.create(nombre=data['equipo'], pais=data['pais'], liga=data['liga'], copasGanadas=data['copas_ganadas'])
            return redirect('equipos')
        else:
            formulario = EquipoForm()
        return render(request, 'blog/equiposFormulario.html')

def busqueda_equipo(request):
    return render(request, 'blog/busquedaEquipo.html')

def buscar(request):
    copasGanadas = request.GET.get("copas_ganadas")
    
    if copasGanadas:
        equipo = Equipo.objects.filter(copasGanadas=copasGanadas)

        return render(request, 'blog/buscar.html', 
            {'equipos': equipo, 'copas_ganadas': copasGanadas})
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

def equipos_formulario(request):
    pass

def equipos(request):
    return render(request,
        'blog/equipos.html',
        {'equipos': Equipo.objects.all() }
        )

def jugador(request):
    return render(request,
        'blog/jugador.html',
        {'jugador': Jugador.objects.all() }
        )

def director_tecnico(request):
    return render(request,
        'blog/director_tecnico.html',
        {'director_tecnico': DirectorTecnico.objects.all() }
        )

def equipo_add(request):
    if request.method == 'POST':
        formulario = EquipoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Equipo.objects.create(
                nombre=data['nombre'],
                pais=data['pais'],
                liga=data['liga'],
                copasGanadas=data['copas_ganadas']
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
                copasGanadas=data['copas_ganadas'],
                equipo=data['equipo'],
                goles=data['goles'],
                )
            return redirect('jugador')
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
                copasGanadas=data['copas_ganadas'],
                equipo=data['equipo'],
                aniosExperiencia=data['anios_experiencia'],
                )
            return redirect('director_tecnico')
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

    return redirect('equipos')

def director_tecnico_delete(request, id_director_tecnico):
    director_tecnico = Jugador.objects.get(id=id_director_tecnico) 
    director_tecnico.delete()

    return redirect('equipos')

def equipo_update(request, id_equipo):
    equipo = Equipo.objects.get(id=id_equipo) 

    if request.method == 'POST':
        formulario = EquipoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
          
            equipo.nombre = data['nombre']
            equipo.pais=data['pais']
            equipo.liga=data['liga']
            equipo.copasGanadas=data['copas_ganadas']

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
            jugador.pais=data['pais']
            jugador.liga=data['liga']
            jugador.copasGanadas=data['copas_ganadas']

            jugador.save()  
            
            return redirect('jugador')
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
            director_tecnico.pais=data['pais']
            director_tecnico.liga=data['liga']
            director_tecnico.copasGanadas=data['copas_ganadas']

            director_tecnico.save()  
            
            return redirect('director_tecnico')
    else:
        formulario = DirectorTecnicoForm(model_to_dict(director_tecnico))
    return render(request, 'blog/equiposFormulario.html', {'formulario': formulario})
