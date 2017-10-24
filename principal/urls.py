from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='principal_index'),
    
    url(r'^crear_nacionalidad/$', views.crear_nacionalidad, name='crear_nacionalidad'),
    url(r'^(?P<id>\d+)/editar_nacionalidad$',views.editar_nacionalidad, name='editar_nacionalidad'),
    url(r'^(?P<id>\d+)/borrar_nacionalidad$',views.borrar_nacionalidad, name='borrar_nacionalidad'),

    url(r'^crear_nivel_instruccion/$', views.crear_nivel_instruccion, name='crear_nivel_instruccion'),
    url(r'^(?P<id>\d+)/editar_nivel_instruccion$',views.editar_nivel_instruccion, name='editar_nivel_instruccion'),
    url(r'^(?P<id>\d+)/borrar_nivel_instruccion$',views.borrar_nivel_instruccion, name='borrar_nivel_instruccion'),

    url(r'^crear_regimen_tenencia/$', views.crear_regimen_tenencia, name='crear_regimen_tenencia'),
    url(r'^(?P<id>\d+)/editar_regimen_tenencia$', views.editar_regimen_tenencia, name='editar_regimen_tenencia'),
    url(r'^(?P<id>\d+)/borrar_regimen_tenencia$', views.borrar_regimen_tenencia, name='borrar_regimen_tenencia'),

    url(r'^crear_anio_construccion/$', views.crear_anio_construccion, name='crear_anio_construccion'),
    url(r'^(?P<id>\d+)/editar_anio_construccion$', views.editar_anio_construccion, name='editar_anio_construccion'),
    url(r'^(?P<id>\d+)/borrar_anio_construccion$', views.borrar_anio_construccion, name='borrar_anio_construccion'),
]
