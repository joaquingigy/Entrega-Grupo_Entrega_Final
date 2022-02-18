
from django.contrib.auth.forms import UserCreationForm
import django.forms as forms 
from django.contrib.auth.models import User


class UserRegisterForm (UserCreationForm):
    
    email = forms.EmailField ()
    password1= forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label='Repetir la Contraseña', widget= forms.PasswordInput)


    class Meta:
        model = User 
        fields = ['username','email', 'password1', 'password2' ]   
        help_texts = {k:"" for k in fields}
        
        
        
        
