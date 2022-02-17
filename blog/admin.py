from django.contrib import admin

# Register your models here.
from .models import Jugador, Equipo, DirectorTecnico, Blog, Autor
admin.site.register (Jugador)
admin.site.register (Equipo)
admin.site.register (DirectorTecnico)
admin.site.register (Blog)
admin.site.register (Autor)