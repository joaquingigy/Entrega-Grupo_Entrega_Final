from django.shortcuts import render
from django.http import HttpResponse
from AppModels.models import Equipo

def crear_equipo(request, nombre, copas_ganadas):
    equipo = Equipo(nombre=nombre, copas_ganadas=copas_ganadas)
    equipo.save()

    return HttpResponse(f'Equipo {nombre} creado! Tiene {copas_ganadas} copas ganadas!')  
