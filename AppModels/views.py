from django.shortcuts import render, redirect
from django.http import HttpResponse

from AppModels.forms import DirectorTecnicoFormulario, EquipoFormulario, JugadorFormulario
from AppModels.models import DirectorTecnico, Equipo, Jugadores

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
    return render(request, 'AppModels/jugador.html',
    {'jugadores':Jugadores.objects.all()})

def director_tecnico(request):
    return render(request, 'AppModels/director_tecnico.html',
    {'directores_tecnicos':DirectorTecnico.objects.all()})

def equipos_formulario(request):
    if request.method == 'POST':

        formulario=EquipoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            Equipo.objects.create(nombre=data['equipo'], copas_ganadas=data['copas_ganadas'])
            return redirect('equipo')
    else:
        formulario=EquipoFormulario()
    return render (request, 'AppModels/equiposFormulario.html',{'formulario':formulario})

def director_tecnico_formulario(request):
    if request.method == 'POST':
        formulario1=DirectorTecnicoFormulario(request.POST)
        
        if formulario1.is_valid():
            data1 = formulario1.cleaned_data
            DirectorTecnico.objects.create(nombre=data1['nombre'], apellido=data1['apellido'])
            return redirect('director_tecnico')
    else:
        formulario1=DirectorTecnicoFormulario()
    return render (request, 'AppModels/directortecnicoFormulario.html',{'formulario1':formulario1})

def jugador_formulario(request):
    if request.method == 'POST':
        formulario2=JugadorFormulario(request.POST)
        
        if formulario2.is_valid():
            data2 = formulario2.cleaned_data
            Jugadores.objects.create(nombre=data2['nombre'], apellido=data2['apellido'], cantidad_goles=data2['cantidad_goles'])
            return redirect('jugador')
    else:
        formulario2=JugadorFormulario()
    return render (request, 'AppModels/jugadorFormulario.html',{'formulario2':formulario2})
    
def busqueda_copas_ganadas(request):
    return render(request, 'AppModels/busquedaCopasGanadas.html')

def buscar(request):
    
    copas_ganadas=request.GET['copas_ganadas']
    
    equipos = Equipo.objects.filter(copas_ganadas=copas_ganadas)
    return render(request, 'AppModels/buscar.html',
            {'equipos': equipos, 'copas_ganadas':copas_ganadas})
