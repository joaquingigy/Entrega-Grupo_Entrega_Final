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