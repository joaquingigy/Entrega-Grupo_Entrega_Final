
from django.contrib.auth.forms import UserCreationForm
import django.forms as forms
from django.contrib.auth.models import User


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

class UsereditForm (UserCreationForm):
    #Acá se definen las opciones que queres modificar del usuario,
    #Ponemos las básicas
    email = forms.EmailField (label= "Modificar E-Mail")
    password1 = forms.CharField (label= 'Contraseña', widget = forms.PasswordInput)
    password1 = forms.CharField (label = 'Repetir la contraseña', widget = forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name = forms.CharField()
    
      
    
    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2','last_name','first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k: "" for k in fields}
            
class AvatarFormulario(forms.Form):
    imagen = forms.ImageField (required = True) 
        
