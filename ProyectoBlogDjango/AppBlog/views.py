from django.shortcuts import render,redirect
from .models import Pelicula,Comentario,Contacto, Perfil,Post
#from .forms import PeliculaFormulario, PeliculaUrlFormulario,ComentarioFormulario
from django.http import HttpResponseRedirect
from AppBlog.forms import PeliculaFormulario,ContactoFormulario,UserRegisterForm,ComentarioFormulario,PerfilFormulario,UpdateUserForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Contacto
from .forms import ContactoFormulario
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.views.generic.edit import UpdateView,DeleteView,CreateView

from django.views.generic.base import TemplateView



from django.utils.decorators import method_decorator


from django.contrib import messages

# Create you
# Create your views here.

from django.db.models import Q 

def Inicio(request):
      search_post = request.GET.get('search')
      post_list=''
      if search_post:
            post_list = Post.objects.filter(Q(titulo__icontains=search_post) | Q(contenido__icontains=search_post))
      else:
            post_list = Post.objects.filter(status=1).order_by('-creado')
      return render(request, "AppBlog/posts.html" ,{'post_list':post_list})


def acerca(request):
      return render(request, "AppBlog/acerca.html")


def PostDelete(request, post_id):
      try:
            post =Post.objects.get(id=post_id,creadopor=request.user)
            post.delete()
            messages.success(request, "Se ha eliminado existosamente el Post!")
            return redirect('PostUsuarios')
      except Post.DoesNotExist:
            messages.error(request, "No se ha podido eliminar el Post!")
            return redirect('PostUsuarios')


class PostUpdate(UpdateView):

      model = Post
      success_url = "post"
      fields = ['titulo','contenido','status']
      def form_valid(self, form):
            form.instance.creadopor = self.request.user
            super(PostUpdate, self).form_valid(form)
            messages.success(self.request, "Se han realizado los cambios exitosamente en el Post!")
            return redirect('PostUsuarios')
      

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
                  mensaje= 'Fue enviado Exitosamente el mensaje!'
                  return render(request, "AppBlog/contacto.html",{"miFormulario":miFormulario,"mensaje":mensaje}) #Vuelvo al inicio o a donde quieran

      else: 
            mensaje=''
            miFormulario= ContactoFormulario() #Formulario vacio para construir el html

      return render(request, "AppBlog/contacto.html", {"miFormulario":miFormulario,"mensaje":mensaje})


from django.core.paginator import Paginator


class PostListar(ListView):
      model=Post
      queryset = Post.objects.filter(status=1).order_by('-creado')
      paginate_by = 4
      template_name = 'posts.html'
     
#class PostDetalle(DetailView):
#      model = Post
#      template_name = 'post_detalle.html'

class PostUsuarios(ListView):
      model=Post
      paginate_by = 4
      template_name = 'posts_usuarios.html'
      def get_queryset(self):
        queryset = super(PostUsuarios, self).get_queryset()
        queryset = queryset.filter(creadopor=self.request.user)
        return queryset

class PostCrear(CreateView):

      model = Post
      success_url = "post"
      fields = ['titulo','contenido','status']
      def form_valid(self, form):
            form.instance.creadopor = self.request.user
            messages.success(self.request, "Se ha creado el Post Exitosamente!")
            return super(PostCrear, self).form_valid(form)
      

                  
      
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
                  messages.success(request, "Se ha creado exitosamente el Usuario!")
                  return render(request,"AppBlog/InicioTemplate.html")

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppBlog/registro.html" ,  {"form":form})

import os

@login_required
def profile(request):
      
      if request.method == 'POST':
            print(request.user.perfil)
            print(request.POST['biografia'])
            user_form = UpdateUserForm(request.POST, instance=request.user)
            form_perfil =PerfilFormulario(request.POST,
                                          request.FILES,
                                          request.POST['biografia'],
                                          instance=request.user.perfil)
            #if form_perfil.is_valid():
            if user_form.is_valid() and form_perfil.is_valid():
                  user_form.save()
                  form_perfil.save()
                  messages.success(request, "Se ha actualizo exitosamente el Perfil!")
                  perfilFormulario=PerfilFormulario(instance=request.user.perfil)
            else:
                  print('eeror al intentar guardar')
      else:
            user_form = UpdateUserForm(instance=request.user)
            perfilFormulario=PerfilFormulario(instance=request.user.perfil)
            print(request.method)
            
      user_profile=Perfil.objects.get(usuario=request.user)            

      return render(request, "AppBlog/perfil.html",{"user_profile":user_profile,"perfilFormulario":perfilFormulario,"user_form": user_form})


from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
      template_name = 'AppBlog/change_password.html'
      success_message = "Se ha realizado el Cambio de Password Exitosamente!"
      success_url = reverse_lazy('Inicio')