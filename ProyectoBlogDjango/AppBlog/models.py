from django.db import models
# Create your models here.
from ckeditor.fields import RichTextField

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


STATUS = (
    (0,"Borrador"),
    (1,"Publicado")
)


#Importo para la relacion con USER
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario=models.OneToOneField(User,on_delete=models.CASCADE)
    biografia=models.CharField(max_length=200)
    image = models.ImageField(upload_to='avatares', null=True, blank = True)

    
    def __str__(self):
        return f'{self.usuario.username} Profile'



from ProyectoBlogDjango.utils import unique_slug_generator
from django.db.models.signals import pre_save,post_save
from .signals import create_profile
   
post_save.connect(create_profile,sender=User)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=True,blank=True)
    actualizado = models.DateTimeField(auto_now= True)
    contenido = RichTextField()#models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo

def slug_generator(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(slug_generator,sender=Post)



class Comentario(models.Model):
    nombre=models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    email=models.EmailField(max_length=100)
    contenido=models.CharField(max_length=5000,null = False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    fechacreado=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fechacreado',)

    def __str__(self):
        return 'Comentario de {}'.format(self.nombre)
    
    


