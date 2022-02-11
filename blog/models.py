from django.db import models

from AppModels.views import equipo

# Create your models here.
class Autor(models.Model):
    nombreDeUsuario = models.CharField(max_length=30)
    clave = models.CharField(max_length=30)
    avatar = models.URLField()
    def __str__(self):
        return self.nombreDeUsuario

class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    autor = models.ForeignKey(
        Autor ,
        on_delete = models.RESTRICT ,
    )
    fechaDePublicacion = models.DateTimeField(auto_now=True)
    urlName = 'blog'
    def __str__(self):
        return self.titulo
    
    
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)
    liga = models.CharField(max_length=1)
    copasGanadas = models.IntegerField(default=0)
    urlName = 'equipo'
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
    
    
class DirectorTecnico(Persona):
    aniosExperiencia = models.IntegerField(default=0)