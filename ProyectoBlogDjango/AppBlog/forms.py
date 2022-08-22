from django import forms

class PeliculaFormulario(forms.Form):

    #Especificar los campos
    titulo = forms.CharField()
    fechaDeEstreno = forms.DateField()
    descripcion = forms.CharField()
    imagen = forms.CharField()


from .models import Contacto

class ContactoFormulario(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'cuerpo')