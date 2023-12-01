from django.urls import path
from . import views



urlpatterns = [

    
    
    path('inicio/front/', views.front, name='front'),
    #USUARIOS

    path('usuarios/', views.index_usuarios, name='index_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),

    #TIPOSNOVEDADES

    path('tiposNovedades/', views.index_tipos_novedades, name='index_tipos_novedades'),
    path('tiposNovedades/crear/', views.crear_tipo_novedad, name='crear_tipo_novedad'),
    path('tiposNovedades/editar/<int:pk>/', views.editar_tipo_novedad, name='editar_tipo_novedad'),
    path('tiposNovedades/eliminar/<int:pk>/', views.eliminar_tipo_novedad, name='eliminar_tipo_novedad'),

    #NOVEDADES

    path('novedades/', views.index_novedades, name='index_novedades'),
    path('novedades/crear/', views.crear_novedad, name='crear_novedad'),
    path('novedades/editar/<int:pk>/', views.editar_novedad, name='editar_novedad'),
    path('novedades/eliminar/<int:pk>/', views.eliminar_novedad, name='eliminar_novedad'),

    #USUARIOSNOVEDADES

    path('usuarios_novedades/', views.index_usuarios_novedades, name='index_usuarios_novedades'),
    path('usuarios_novedades/crear/', views.crear_usuarios_novedad, name='crear_usuarios_novedad'),
    path('usuarios_novedades/editar/<int:pk>/', views.editar_usuarios_novedad, name='editar_usuarios_novedad'),
    path('usuarios_novedades/eliminar/<int:pk>/', views.eliminar_usuarios_novedad, name='eliminar_usuarios_novedad'),

    #login
    path('', views.welcome, name='welcome'),
    path('welcome/', views.welcome, name='welcome'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
]
