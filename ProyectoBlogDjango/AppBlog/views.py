from django.shortcuts import render,redirect
from .models import Pelicula,Comentario,Contacto, Perfil,Post
#from .forms import PeliculaFormulario, PeliculaUrlFormulario,ComentarioFormulario
from django.http import HttpResponseRedirect
from AppBlog.forms import PeliculaFormulario,ContactoFormulario,UserRegisterForm,ComentarioFormulario,PerfilFormulario

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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

from django.views.generic.base import TemplateView


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



from django.utils.decorators import method_decorator








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
      model=Post
      queryset = Post.objects.filter(status=1).order_by('-creado')
      template_name = 'posts.html'
     
#class PostDetalle(DetailView):
#      model = Post
#      template_name = 'post_detalle.html'




class PostCrear(CreateView):

      model = Post
      success_url = "post"
      fields = ['titulo','contenido','status']
      

                  
      
#class PostDetalle(DetailView):
#      model = Post
#      template_name = 'AppBlog/post_detalle.html'
#      context_object_name = 'object'


def PostDetalle(request,slug):
      post = Post.objects.get(slug=slug)
      if( request.method == 'POST'):
            form = ComentarioFormulario(request.POST)

            if(form.is_valid()):
                  comentario=form.save(commit=False)
                  comentario.nombre=request.user      #Le asigno el valor del userlogueadp(esta relacionado por FK con User)
                  comentario.post=post
                  comentario.save()
                  
                  return redirect('PostDetalle',slug=post.slug)
      else:
            form=ComentarioFormulario() 
      return render(request,'AppBlog/post_detalle.html',{'post':post,'form':form})


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate





def login_request(request):

      if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():  # Si pasó la validación de Django

                  usuario = form.cleaned_data.get('username')
                  contrasenia = form.cleaned_data.get('password')

                  user = authenticate(username= usuario, password=contrasenia)

                  if user is not None:
                        login(request, user)

                        #    return render(request, "AppBlog/InicioTemplate.html", {"mensaje":f"Bienvenido {usuario}"})
                        return render(request, "AppBlog/InicioTemplate.html", {"usuario": usuario})
                  else:
                        return render(request, "AppBlog/InicioTemplate.html", {"usuario":"Datos incorrectos"})
            
            else:

                  return render(request, "AppBlog/InicioTemplate.html", {"usuario":"Formulario erroneo"})

      form = AuthenticationForm()

      return render(request, "AppBlog/login.html", {"form": form})


# Vista de registro
def register(request):

      if request.method == 'POST':

           # form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppBlog/InicioTemplate.html" ,  {"mensaje":"Usuario Creado "})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppBlog/registro.html" ,  {"form":form})

import os

@login_required
def profile(request):
      
      if request.method == 'POST':
            print(request.user.perfil)
            form_perfil =PerfilFormulario(request.POST,
                                          request.FILES,
                                          request.POST['biografia'],
                                          instance=request.user.perfil)
            if form_perfil.is_valid():
                  form_perfil.save()
                  mensaje= 'Se han guardado los cambios Exitosamente!'              
            else:
                  print('eeror al intentar guardar')
      else:
            mensaje='que onda else'
            print(request.method)
            
      user_profile=Perfil.objects.get(usuario=request.user)            
      perfilFormulario= PerfilFormulario() #Formulario vacio para construir el html 
      print(mensaje)

      return render(request, "AppBlog/perfil.html",{"user_profile":user_profile,"perfilFormulario":perfilFormulario,"mensaje":mensaje})