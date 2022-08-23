# ProyectoBlogDjango
Este sistema permite acceder a:

- Peliculas: podes dar de Alta, Modificar, Eliminar una Pelicula
- Blog: crear un post.
- Contacto: Contactarse con el administrador por medio del módulo "Contacto".
- Buscar: En el header tenes la posibilidad de buscar algun Post creado.

Este codigo contiene:
Vistas
Formularios
Modelos
Templates
Urls

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

## Instalar django-crispy
```$pip install django-crispy-forms ```

## Clonar el projecto con git
windows:

```C:\> git clone https://github.com/pablofrivero/ProyectoBlogDjango.git```

Linux/Mac:

```$ git clone https://github.com/pablofrivero/ProyectoBlogDjango.git```

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
