from calendar import c
from attr import attrs
from django.contrib.auth.forms import UserCreationForm
import django.forms as forms
from django.contrib.auth.models import User
from django.forms import Form, CharField, ImageField, IntegerField ,DateTimeField,ModelChoiceField

from blog.models import Avatar, Blog, Jugador,Equipo
# from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE


class UserRegisterForm (UserCreationForm):
    
    email = forms.EmailField ()
    password1= forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget= forms.PasswordInput)

    
    #Agregado Clase de Avatar para Editar Perfil 
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User 
        fields = ['username','email', 'password1', 'password2','last_name','first_name']   
        help_texts = {k:"" for k in fields}

class UserEditForm (UserCreationForm):
    #Acá se definen las opciones que queres modificar del usuario,
    #Ponemos las básicas
    email = forms.EmailField (label= "Modificar E-Mail")
    password1 = forms.CharField (label= 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField (label = 'Repetir la contraseña', widget = forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()
    
      
    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2','last_name','first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}
            
# class AvatarFormulario(forms.Form):
#     imagen = forms.ImageField (required = True) 

class EquipoForm(Form):
    nombre = CharField(max_length=40)
    pais = CharField(max_length=30)
    liga = CharField(max_length=1)
    copasGanadas = IntegerField() 

    class Meta:
        model = Equipo
        fields = [ 'nombre', 'pais', 'liga','copasGanadas'] 
        #Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}

class JugadorForm(Form):
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    copasGanadas = IntegerField()
    equipo =ModelChoiceField (queryset = Equipo.objects.all()) 
    goles = IntegerField()

    class Meta:
        model = Jugador
        fields = [ 'nombre', 'apellido', 'copasGanadas','equipo','goles'] 
        #Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}




class DirectorTecnicoForm(Form):
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
    copasGanadas = IntegerField(label= 'Copas Ganadas')
    equipo = ModelChoiceField (queryset = Equipo.objects.all()) 
    aniosExperiencia = IntegerField(label= 'Años Experiencia')
        
        
class BlogForm(Form):
    titulo= CharField(max_length=50)
    subtitulo= CharField(max_length=50)
    cuerpo = CharField(widget=TinyMCE (attrs = {'cols' : 80 ,'rows' : 30 }))
    autor = ModelChoiceField (queryset = User.objects.all())
    imagen = CharField ()
    class Meta:
        model = Blog
        fields = [ 'titulo','subtitulo', 'cuerpo', 'autor','imagen'] 
        #Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}
        #model = FlatPage
    
class AvatarFormulario (Form):
    imagen = ImageField (required = True)
    class Meta:
        model = Avatar
        fields = ['imagen'] 
        #Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}        
