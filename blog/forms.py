from django.contrib.auth.forms import UserCreationForm
import  django.forms as forms 
from django.contrib.auth.models import User
from django.forms import Form, CharField, IntegerField



class UserRegisterForm (UserCreationForm):
    
    email = forms.EmailField ()
    password1= forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget= forms.PasswordInput)


    class Meta:
        model = User 
        fields = ['username','email', 'password1', 'password2' ]   
        help_texts = {k:"" for k in fields}

class EquipoForm(Form):
    nombre = CharField(max_length=40)
    pais = CharField(max_length=30)
    liga = CharField(max_length=1)
    copasGanadas = IntegerField(default=0) 


class JugadorForm(Form):
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    copasGanadas = IntegerField(default=0)
    equipo = CharField(max_length=40)
    goles = IntegerField(default=0)


class DirectorTecnicoForm(Form):
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    copasGanadas = IntegerField(default=0)
    equipo = CharField(max_length=40)
    aniosExperiencia = IntegerField(default=0)
        
        
        
        
