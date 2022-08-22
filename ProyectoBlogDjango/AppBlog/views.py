from django.shortcuts import render
from .models import Pelicula,Comentario,Informacion
#from .forms import PeliculaFormulario, PeliculaUrlFormulario,ComentarioFormulario
from django.http import HttpResponseRedirect
from django.contrib import messages
from AppBlog.forms import PeliculaFormulario

# Create you
# Create your views here.

from django.db.models import Q 

def Inicio(request):
      search_post = request.GET.get('search')
      peliculas=''
      if search_post:
            peliculas = Pelicula.objects.filter(Q(titulo__icontains=search_post) | Q(descripcion__icontains=search_post))
      #else:
      #      peliculas = Pelicula.objects.all().order_by('fechaDeCreacion')
      return render(request, "AppBlog/InicioTemplate.html" ,{'peliculas':peliculas})


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
