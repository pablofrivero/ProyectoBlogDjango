from django import forms
import datetime
class PeliculaFormulario(forms.Form):

    #Especificar los campos
    titulo = forms.CharField()
    fechaDeEstreno =  forms.DateField(widget=forms.widgets.DateInput({'type': 'date'}))
                                
    descripcion = forms.CharField(widget=forms.Textarea)
    imagen = forms.CharField()


from .models import Contacto,Post,Comentario,Perfil

class ContactoFormulario(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'cuerpo')
        
        
        
class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'contenido','status')
        
        

#Para formulario de registro de usuario
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               label="Usuario",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             label="Email",
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

# Formulario Comentario
class ComentarioFormulario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4}),
        }


#Formulario Perfil
class PerfilFormulario(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre','apellido','image','link','biografia']
        widgets = {
            'biografia': forms.Textarea(attrs={'rows': 4}),
        }