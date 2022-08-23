from django.shortcuts import render
from .models import Pelicula,Comentario,Contacto,Post
#from .forms import PeliculaFormulario, PeliculaUrlFormulario,ComentarioFormulario
from django.http import HttpResponseRedirect
from AppBlog.forms import PeliculaFormulario,ContactoFormulario

# Create you
# Create your views here.

from django.db.models import Q 

def Inicio(request):
      search_post = request.GET.get('search')
      post_list=''
      if search_post:
            post_list = Post.objects.filter(Q(titulo__icontains=search_post) | Q(contenido__icontains=search_post))
  
      return render(request, "AppBlog/posts.html" ,{'post_list':post_list})


def peliculas(request):

      if request.method == 'POST':

            miFormulario = PeliculaFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  pelicula = Pelicula (titulo=informacion['titulo'], 
                                       fechaDeEstreno=informacion['fechaDeEstreno'],
                                       descripcion=informacion['descripcion'],
                                        imagen=informacion['imagen']) 

                  pelicula.save()

                  return render(request, "AppBlog/InicioTemplate.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PeliculaFormulario() #Formulario vacio para construir el html

      return render(request, "AppBlog/peliculas.html", {"miFormulario":miFormulario})



from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.views.generic.edit import UpdateView,DeleteView,CreateView


class PeliculaList(ListView):
      #ver url https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Generic_views
    model = Pelicula
    queryset = Pelicula.objects.all()#.filter(titulo='Desarrollo') ##Aca le agrege un filtro
    template_name = "AppBlog/peliculas_list.html"

class PeliculaDetalle(DetailView):

    model = Pelicula
    template_name = "AppBlog/pelicula_detalle.html"

class PeliculaCreacion(CreateView):

    model = Pelicula
    success_url = "/AppBlog/pelicula/list"
    fields = ['titulo', 'fechaDeEstreno','descripcion','imagen']

class PeliculaUpdate(UpdateView):

    model = Pelicula
    success_url = "/AppBlog/pelicula/list"
    fields = ['titulo', 'fechaDeEstreno','descripcion','imagen']

class PeliculaDelete(DeleteView):

    model = Pelicula
    success_url = "/AppBlog/pelicula/list"



from .models import Contacto
from .forms import ContactoFormulario
from django.shortcuts import render

def contacto(request):
      
      if request.method == 'POST':

            miFormulario = ContactoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  contacto = Contacto (   nombre=informacion['nombre'], 
                                          email=informacion['email'],
                                          cuerpo=informacion['cuerpo']
                                          ) 

                  contacto.save()
                  mensaje= 'Fue enviado Exitosamente!'
                  return render(request, "AppBlog/contacto.html",{"miFormulario":miFormulario,"mensaje":mensaje}) #Vuelvo al inicio o a donde quieran

      else: 
            mensaje=''
            miFormulario= ContactoFormulario() #Formulario vacio para construir el html

      return render(request, "AppBlog/contacto.html", {"miFormulario":miFormulario,"mensaje":mensaje})




class PostListar(ListView):
      queryset = Post.objects.filter(status=1).order_by('-creado')
      template_name = 'posts.html'

class PostDetalle(DetailView):
      model = Post
      template_name = 'post_detalle.html'

class PostCrear(CreateView):
      model = Post
      success_url = "post"
      fields = ['titulo', 'slug','contenido','status']