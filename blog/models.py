# from pyexpat import model
from django.db import models

# from AppModels.views import equipo

from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
# class Autor(models.Model):
#     nombreDeUsuario = models.CharField(max_length=30)
#     clave = models.CharField(max_length=30)
#     avatar = models.URLField()
#     def __str__(self):
#         return self.nombreDeUsuario

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo= models.CharField(max_length=50)
    cuerpo = HTMLField()
    autor = models.ForeignKey(
        User ,
        on_delete = models.RESTRICT ,
    )
    fechaDePublicacion = models.DateTimeField(auto_now=True)
    urlNombre = 'blog'
    urlUpdate = "blog_update"
    urlDelete = "blog_delete"
    imagen = models.URLField()
    def __str__(self):
        return self.titulo
   
   
    
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)
    liga = models.CharField(max_length=1)
    copasGanadas = models.IntegerField(default=0)
    urlNombre = 'equipo'
    urlUpdate = "equipo_update"
    urlDelete = "equipo_delete"
    def __str__(self): 
        return self.nombre
    
    
    
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    copasGanadas = models.IntegerField(default=0)
    equipo = models.ForeignKey(
        Equipo ,
        on_delete=models.SET_NULL,
        null=True
    )
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
  
    
class Jugador(Persona):
    goles = models.IntegerField(default=0)
    urlNombre = 'jugador'
    urlUpdate = "jugador_update"
    urlDelete = "jugador_delete"
class DirectorTecnico(Persona):
    aniosExperiencia = models.IntegerField(default=0)
    urlNombre = 'director_tecnico'
    urlUpdate = "director_tecnico_update"
    urlDelete = "director_tecnico_delete"

class Avatar (models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    #Subcarpeta avatares de media
    imagen = models.ImageField (upload_to = 'avatares', null=True , blank = True)
    