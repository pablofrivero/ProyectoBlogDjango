from django.urls import path

from AppBlog import views

from django.contrib.auth.views import LogoutView,LoginView
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   
    path('', login_required(views.Inicio), name="Inicio"), #esta era nuestra primer view

    path('contacto', views.contacto, name="Contacto"), #esta era nuestra primer view

    path('buscar/', views.Inicio, name="buscar"), #esta era nuestra primer view
    path('acerca/', views.acerca, name='acerca'),

    path('profile', views.profile, name='profile'),

    path('post', login_required(views.PostListar.as_view()), name='Post'),
   # path('<slug:slug>/', views.PostDetalle.as_view(), name='PostDetalle'),
    path('<slug:slug>/', login_required(views.PostDetalle), name='PostDetalle'),
    path(r'^nuevoPost$', login_required(views.PostCrear.as_view()), name='NewPost'),

    path('postusuarios', views.PostUsuarios.as_view(), name='PostUsuarios'),
	path('postdelete/<int:post_id>/', views.PostDelete, name='PostDelete'),
    path(r'^editarPost/(?P<pk>\d+)$', views.PostUpdate.as_view(), name='PostUpdate'),



    path('login', LoginView.as_view(template_name='AppBlog/login.html'), name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name='Logout'),
    path('password-change', views.ChangePasswordView.as_view(), name='password_change'),


] 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)