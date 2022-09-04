
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

## Capturas de cada Módulo:

* Inicio
![inicio-blog](https://user-images.githubusercontent.com/93736464/186167561-9c05eb24-2f61-4cc2-8ea9-1b0f08bb4097.jpg)

* Post
![irPost](https://user-images.githubusercontent.com/93736464/186168537-ea11707b-9460-45e9-b7fa-b63b56982e61.jpg)
![crearpost](https://user-images.githubusercontent.com/93736464/186168550-ff2352fc-dfb1-48f0-9f05-b90a0a2dd82d.jpg)

* Buscar
![buscar](https://user-images.githubusercontent.com/93736464/186168804-53753eac-4e0b-487b-bd42-3e21e2b75210.jpg)

* Contacto
![contacto](https://user-images.githubusercontent.com/93736464/186168918-c0e41d79-2135-4e27-9b6c-4c38901d7e43.jpg)

* Profile

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

