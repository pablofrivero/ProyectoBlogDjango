from django.db import models
# Create your models here.

class Pelicula(models.Model):

    titulo=models.CharField(max_length=40)
    fechaDeEstreno =  models.DateField()
    descripcion=models.CharField(max_length=5000,null = False)
    imagen=models.TextField()
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


STATUS = (
    (0,"Borrador"),
    (1,"Publicado")
)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    actualizado = models.DateTimeField(auto_now= True)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo