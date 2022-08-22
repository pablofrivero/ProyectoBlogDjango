from django.db import models
# Create your models here.

class Pelicula(models.Model):

    titulo=models.CharField(max_length=40)
    fechaDeEstreno =  models.DateField()
    descripcion=models.CharField(max_length=5000,null = False)
    imagen=models.CharField(max_length=50)
    fechaDeCreacion=models.DateTimeField(auto_now_add=True)

class Contacto(models.Model):

    nombre=models.CharField(max_length=5000,null = False)
    email=models.EmailField()
    cuerpo = models.TextField()
    fechaDeCreacion=models.DateTimeField(auto_now_add=True)


class Comentario(models.Model):
    comentario=models.CharField(max_length=5000,null = False)
    usuario=models.CharField(max_length=40,null = False)
    pelicula_id = models.ForeignKey(Pelicula, on_delete=models.SET_NULL, null = True)
    fechaDeCreacion=models.DateTimeField(auto_now_add=True)
