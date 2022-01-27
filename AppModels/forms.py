from django.forms import Form, CharField, IntegerField

class EquipoForm(Form):
    equipo = CharField() 
    copas_ganadas = IntegerField()

class JugadorForm(Form):
    jugador = CharField()
    apellido = CharField()
    cantidad_goles = IntegerField()

class DirectorTecnicoForm(Form):
    nombre = CharField()
    apellido = CharField()

 