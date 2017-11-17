from django.conf.urls import url

from . import views

urlpatterns = [
    


    url(r'^$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^cambiar_password/$', views.cambiar_password, name='cambiar_password'),
    url(r'^recuperar_password/$', views.recuperar_password, name='recuperar_password'),


    url(r'^obtener_puntos/$', views.obtener_puntos, name='obtener_puntos'),

    url(r'^principal/$', views.principal, name='principal'),


    url(r'^crear_usuario/$', views.crear_usuario, name='crear_usuario'),
    url(r'^(?P<id>\d+)/editar_usuario$', views.editar_usuario, name='editar_usuario'),
    url(r'^(?P<id>\d+)/borrar_usuario$', views.borrar_usuario, name='borrar_usuario'),

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

    url(r'^crear_material_estructura/$', views.crear_material_estructura, name='crear_material_estructura'),
    url(r'^(?P<id>\d+)/editar_material_estructura$', views.editar_material_estructura, name='editar_material_estructura'),
    url(r'^(?P<id>\d+)/borrar_material_estructura$', views.borrar_material_estructura, name='borrar_material_estructura'),

    url(r'^crear_tipo_produccion/$', views.crear_tipo_produccion, name='crear_tipo_produccion'),
    url(r'^(?P<id>\d+)/editar_tipo_produccion$', views.editar_tipo_produccion, name='editar_tipo_produccion'),
    url(r'^(?P<id>\d+)/borrar_tipo_produccion$', views.borrar_tipo_produccion, name='borrar_tipo_produccion'),

    url(r'^crear_eleccion_cultivo/$', views.crear_eleccion_cultivo, name='crear_eleccion_cultivo'),
    url(r'^(?P<id>\d+)/editar_eleccion_cultivo$', views.editar_eleccion_cultivo, name='editar_eleccion_cultivo'),
    url(r'^(?P<id>\d+)/borrar_eleccion_cultivo$', views.borrar_eleccion_cultivo, name='borrar_eleccion_cultivo'),

    url(r'^crear_tipo_cultivo/$', views.crear_tipo_cultivo, name='crear_tipo_cultivo'),
    url(r'^(?P<id>\d+)/editar_tipo_cultivo$', views.editar_tipo_cultivo, name='editar_tipo_cultivo'),
    url(r'^(?P<id>\d+)/borrar_tipo_cultivo$', views.borrar_tipo_cultivo, name='borrar_tipo_cultivo'),

    url(r'^crear_especie/$', views.crear_especie, name='crear_especie'),
    url(r'^(?P<id>\d+)/editar_especie$', views.editar_especie, name='editar_especie'),
    url(r'^(?P<id>\d+)/borrar_especie$', views.borrar_especie, name='borrar_especie'),

    url(r'^crear_factor_climatico/$', views.crear_factor_climatico, name='crear_factor_climatico'),
    url(r'^(?P<id>\d+)/editar_factor_climatico$', views.editar_factor_climatico, name='editar_factor_climatico'),
    url(r'^(?P<id>\d+)/borrar_factor_climatico$', views.borrar_factor_climatico, name='borrar_factor_climatico'),

    url(r'^crear_triple_lavado/$', views.crear_triple_lavado, name='crear_triple_lavado'),
    url(r'^(?P<id>\d+)/editar_triple_lavado$', views.editar_triple_lavado, name='editar_triple_lavado'),
    url(r'^(?P<id>\d+)/borrar_triple_lavado$', views.borrar_triple_lavado, name='borrar_triple_lavado'),

    url(r'^crear_asesoramiento/$', views.crear_asesoramiento, name='crear_asesoramiento'),
    url(r'^(?P<id>\d+)/editar_asesoramiento$', views.editar_asesoramiento, name='editar_asesoramiento'),
    url(r'^(?P<id>\d+)/borrar_asesoramiento$', views.borrar_asesoramiento, name='borrar_asesoramiento'),
]
