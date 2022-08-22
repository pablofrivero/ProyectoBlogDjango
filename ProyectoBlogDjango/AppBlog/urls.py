from django.urls import path

from AppBlog import views


urlpatterns = [
   
    path('', views.Inicio, name="Inicio"), #esta era nuestra primer view
    #path('Inicio', views.PeliculaCreacion, name="RegistrarPelicula"), #esta era nuestra primer view
    path('peliculas', views.peliculas, name="Peliculas"), #esta era nuestra primer view
   # path('GuardarPelicula', views.GuardarPelicula, name="GuardarPelicula"), #esta era nuestra primer view
    #path('EliminarPelicula/<int:id>',views.EliminarPelicula,name="EliminarPelicula"),  
   # path('EditarPelicula/<int:id>/', views.EditarPelicula, name="EditarPelicula"),
   # path('GuardarPeliculaUrl', views.GuardarPeliculaUrl, name="GuardarPeliculaUrl"),

    #path('ComentarPelicula/<int:id>/', views.ComentarPelicula, name="ComentarPelicula"),
    path('buscar/', views.peliculas, name="buscar"), #esta era nuestra primer view

    ##Referencias a las clases en las vistas de
    path('pelicula/list', views.PeliculaList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.PeliculaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.PeliculaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.PeliculaUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PeliculaDelete.as_view(), name='Delete'),

]
