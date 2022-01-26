from django.shortcuts import render,redirect
from django.http import HttpResponse
from AppModels.models import Equipo

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
        equipo =request.POST['equipo']
        copas_ganadas=request.POST['copas_ganadas']
        print(request.POST)
        Equipo.objects.create(nombre=equipo, copas_ganadas=copas_ganadas)
        return redirect('equipo')
    return render (request, 'AppModels/equiposFormulario.html')
    