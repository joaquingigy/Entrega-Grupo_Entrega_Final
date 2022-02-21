from django.contrib import admin

# Register your models here.
from .models import Avatar, Jugador, Equipo, DirectorTecnico, Blog
admin.site.register (Jugador)
admin.site.register (Equipo)
admin.site.register (DirectorTecnico)
admin.site.register (Blog)
# admin.site.register (Autor)
admin.site.register (Avatar)