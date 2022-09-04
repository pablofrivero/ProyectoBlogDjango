
# ProyectoBlogDjango
Este sistema permite acceder a:

- Blog: crear un post,Editar y eliminar.
- Comentarios: Dentro del Blog podes comentar sobre el Blog.
- Profile: Podes Crear un usuario para acceder al Blog.
- Contacto: Contactarse con el administrador por medio del módulo "Contacto".
- Acerca: Podes saber mas sobre el Blog.
- Buscar: En el header tenes la posibilidad de buscar algun Post creado.

Este codigo contiene:
Vistas
Formularios
Modelos
Templates
Urls
## Un resumen en Video!
[![Alt text]([https://img.youtube.com/vi/configuroweb/0.jpg](https://user-images.githubusercontent.com/93736464/188291750-947434b2-65aa-40e7-91d3-702cef37e054.jpg))](https://youtu.be/1GX3cfIq6fw)

## Capturas de cada Módulo:

* Inicio
![Inicio](https://user-images.githubusercontent.com/93736464/188291750-947434b2-65aa-40e7-91d3-702cef37e054.jpg)

* Post
![PostCrear](https://user-images.githubusercontent.com/93736464/188291760-1c7af063-6acc-43a7-9086-72a4c3ed00c1.jpg)
![PostModificar](https://user-images.githubusercontent.com/93736464/188291765-d86ef134-0450-4725-9fb9-412512db2f82.jpg)

* Contacto
![contacto](https://user-images.githubusercontent.com/93736464/188291798-3520c8d5-3c45-4e1e-a91a-094c84a1cdc7.jpg)

* Profile
![Profile](https://user-images.githubusercontent.com/93736464/188291723-3535c92b-a545-4e05-a03e-77593ead3ab3.jpg)

<p align="right">(<a href="#readme-top">Volver al inicio</a>)</p>
**Importante:** Este ejemplo fue probado con python Python 3.10.4 y Django 4.0.6


```PS C:\> python --version```
Python 3.X.X 
En Linux/Mac tiene que abrir una terminal bash

```$ python --version```
Python 3.X.X 
Si les aparece la versión todo OK pueden seguir. Caso contrario descarguen python desde este link.

## Instalar django
En una terminal cmd o powershell desde windows:

```C:\> pip install django```
Linux/Mac:

```$ pip install django```
Si no arrojo errores esto es suficiente para poder correr el proyecto.
<p align="right">(<a href="#readme-top">Volver al inicio</a>)</p>

## Instalar django-crispy
```$pip install django-crispy-forms ```

## Instalar django-ckeditor
```$pip install django-ckeditor ```


## Clonar el projecto con git
windows:

```C:\> git clone https://github.com/pablofrivero/ProyectoBlogDjango.git```

Linux/Mac:

```$ git clone https://github.com/pablofrivero/ProyectoBlogDjango.git```
<p align="right">(<a href="#readme-top">Volver al inicio</a>)</p>

## Modificar el path donde estan los templates
Abrir el archivo settings.py, ir a TEMPLATES y Modificar en la variable DIRS por lo sig:
```'DIRS': ['C:/ProyectoBlogDjango/ProyectoBlogDjango/AppBlog/templates/AppBlog']```

## Crear usuario Administrador
```python manage.py createsuperuser```

## Correr el Servidor
Los siguinetes comandos son analogos en Mac/Linux/Windows:

```cd ProyectoBlogDjango```

```python manage.py migrate```

La consola mostrara las migraciones de la base de datos que se realizaron.

Luego arrancamos el servidor web

```python manage.py runserver```

Listo! ya tenes corriendo el ejemplo.

Ahora Hace click en el siguiente link para ver el ejemplo corriendo:

Starting development server at 
[http://localhost:8000/] (http://localhost:8000/)

El acceso al sistema creado es :
[http://localhost:8000/AppBlog/](http://127.0.0.1:8000/AppBlog/)
<p align="right">(<a href="#readme-top">Volver al inicio</a>)</p>

