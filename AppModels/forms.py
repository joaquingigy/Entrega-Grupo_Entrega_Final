<<<<<<< HEAD
from django.forms import Form, CharField, IntegerField

class EquipoFormulario(Form):
    equipo=CharField()
    copas_ganadas=IntegerField()
    
class DirectorTecnicoFormulario(Form):
    nombre=CharField()
    apellido=CharField()
    
class JugadorFormulario(Form):
    nombre=CharField()
    apellido= CharField()
    cantidad_goles=IntegerField()
=======
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

 
>>>>>>> 3cbdadb4aa947cb82973f6a68eecd642f1039734
