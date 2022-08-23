from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Contacto)
admin.site.register(Post)

