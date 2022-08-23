from django import forms
import datetime
class PeliculaFormulario(forms.Form):

    #Especificar los campos
    titulo = forms.CharField()
    fechaDeEstreno =  forms.DateField(widget=forms.widgets.DateInput({'type': 'date'}))
                                
    descripcion = forms.CharField(widget=forms.Textarea)
    imagen = forms.CharField()


from .models import Contacto,Post

class ContactoFormulario(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'cuerpo')
        
class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'slug', 'contenido','status')