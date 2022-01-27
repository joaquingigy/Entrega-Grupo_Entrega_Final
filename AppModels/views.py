from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppModels.forms import EquipoForm, JugadorForm, DirectorTecnicoForm
from AppModels.models import DirectorTecnico, Equipo, Jugador

def crear_equipo(request, nombre, copas_ganadas):
    equipo = Equipo(nombre=nombre, copas_ganadas=copas_ganadas)
    equipo.save()

    return HttpResponse(f'Equipo {nombre} creado! Tiene {copas_ganadas} copas ganadas!')  

def inicio(request):
    return render(request, 'AppModels/inicio.html')

def equipo(request):
    return render(request, 'AppModels/equipo.html',
    {'equipos':Equipo.objects.all()})

def jugador(request):
    return render(request, 'AppModels/jugador.html')

def director_tecnico(request):
    return render(request, 'AppModels/director_tecnico.html')

def equipos_formulario(request):
    if request.method == 'POST':
        formulario =  EquipoForm(request.POST) 

        if formulario .is_valid():
            data = formulario.cleaned_data 
            Equipo.objects.create(nombre=data['equipo'], copas_ganadas=data['copas_ganadas'])
            return redirect('equipo')
    else:
         formulario = EquipoForm()  
    return render (request, 'AppModels/equiposFormulario.html', {'formulario': formulario})

def jugadores_formulario(request):
    if request.method == 'POST':
        formulario =  JugadorForm(request.POST) 

        if formulario .is_valid():
            data = formulario.cleaned_data 
            Jugador.objects.create(nombre=data['nombre'], apellido=data['apellido'], cantidad_goles=data['cantidad_goles'])
            return redirect('jugador')
    else:
         formulario = JugadorForm()  
    return render (request, 'AppModels/jugadoresFormulario.html', {'formulario': formulario})

def directores_tecnicos_formulario(request):
    if request.method == 'POST':
        formulario =  DirectorTecnicoForm(request.POST) 

        if formulario .is_valid():
            data = formulario.cleaned_data 
            DirectorTecnico.objects.create(nombre=data['nombre'], apellido=data['apellido'])
            return redirect('director_tecnico')
    else:
         formulario = DirectorTecnicoForm()  
    return render (request, 'AppModels/directores_tecnicosFormulario.html', {'formulario': formulario})    