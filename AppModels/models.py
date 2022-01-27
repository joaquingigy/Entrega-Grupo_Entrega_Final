from django.db.models import Model
from django.db.models.fields import CharField, IntegerField

class Equipo(Model):
    nombre = CharField(max_length=30)
    copas_ganadas = IntegerField()

    def __str__(self):
        return f'Equipo {self.nombre}({self.copas_ganadas})' 

class Jugador(Model):
    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    cantidad_goles = IntegerField()

    def __str__(self):
        return f'Jugador {self.nombre}({self.apellido}) ha metido ({self.cantidad_goles}) en su carrera!' 

class DirectorTecnico(Model):
    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)

    def __str__(self):
        return f'DirectorTecnico {self.nombre}({self.apellido})' 


 



