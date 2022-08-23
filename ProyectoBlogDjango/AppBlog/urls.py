from django.urls import path

from AppBlog import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path('', views.Inicio, name="Inicio"), #esta era nuestra primer view

    path('peliculas', views.peliculas, name="Peliculas"), #esta era nuestra primer view
    path('contacto', views.contacto, name="Contacto"), #esta era nuestra primer view

    path('buscar/', views.peliculas, name="buscar"), #esta era nuestra primer view

    ##Referencias a las clases en las vistas de
    path('pelicula/list', views.PeliculaList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.PeliculaDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.PeliculaCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.PeliculaUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PeliculaDelete.as_view(), name='Delete'),
   
    path('post', views.PostListar.as_view(), name='Post'),
   # path('<slug:slug>/', views.PostDetalle.as_view(), name='PostDetalle'),
    path('<slug:slug>/', views.PostDetalle, name='PostDetalle'),
    path(r'^nuevoPost$', views.PostCrear.as_view(), name='NewPost'),

    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name='Logout'),

]
