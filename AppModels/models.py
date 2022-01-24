from django.db.models import Model
from django.db.models.fields import CharField, IntegerField

class Equipo(Model):
    nombre = CharField(max_length=30)
    copas_ganadas = IntegerField()

class Jugadores(Model):
    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    cantidad_goles = IntegerField()

class DirectorTecnico(Model):
    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)


 



