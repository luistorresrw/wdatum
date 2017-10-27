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

]
