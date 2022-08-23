# ProyectoBlogDjango
Este sistema permite acceder a:
- Peliculas: podes dar de Alta, Modificar, Eliminar una Pelicula
- Blog: crear un post.
- Contacto: Contactarse con el administrador por medio del módulo "Contacto".

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
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    ##    'DIRS': ['C:/ProyectoBlogDjango/ProyectoBlogDjango/AppBlog/templates/AppBlog'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

## Correr el Servidor
Los siguinetes comandos son analogos en Mac/Linux/Windows:

```cd ProyectoBlogDjango```

```python manage.py migrate```

La consola mostrara las migraciones de la base de datos que se realizaron.

## Crear usuario Administrador
```python manage.py createsuperuser```

Luego arrancamos el servidor web

```python manage.py runserver```

Listo! ya tenes corriendo el ejemplo.

Ahora Hace click en el siguiente link para ver el ejemplo corriendo:

Starting development server at 
[http://localhost:8000/] (http://localhost:8000/)

El acceso al sistema creado es :
[http://localhost:8000/](http://127.0.0.1:8000/AppBlog/)
