from django.contrib import admin

# Register your models here.
from .models import Jugadores, Equipo, DirectorTecnico
admin.site.register (Jugadores)
admin.site.register (Equipo)
admin.site.register (DirectorTecnico)
