from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from principal import views
from rest_framework.authtoken import views as token_views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupviewSet)
router.register(r'updates',views.UpdateViewSet)
router.register(r'regimen_tenencia',views.RegimenTenenciaViewSet)
router.register(r'nacionalidad',views.NacionalidadViewSet)
router.register(r'nivel_instrucion',views.NivelInstruccionViewSet)
router.register(r'factor_climatico',views.FactorClimaticoViewSet)
router.register(r'triple_lavado',views.TripleLavadoViewSet)
router.register(r'asesoramiento',views.AsesoramientoViewSet)
router.register(r'material_estructura',views.MaterialEstructuraViewSet)
router.register(r'anio_construccion',views.AnioConstruccionViewSet)
router.register(r'especie',views.EspecieViewSet)
router.register(r'tipo_cultivo',views.TipoCultivoViewSet)
router.register(r'tipo_produccion',views.TipoProduccionViewSet)
router.register(r'eleccion_cultivo',views.EleccionCultivoViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('principal.urls')),
    url(r'^api/',include(router.urls)),
    #url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    #url(r'^api-token-auth/', token_views.obtain_auth_token),
    url(r'^api/auth/', include('rest_auth.urls')),
    url(r'^api/actualizaciones_posteriores_a/(?P<last_update>[0-9]+)/$',views.UpdatesPosteriores),
    url(r'^api/last_update/$',views.lastUpdate),
    url(r'^api/updates_from_mobile/$',views.updates_from_mobile),
    url(r'^api/sincro_establecimiento/$',views.sincro_establecimiento),
    url(r'^api/sincro_familia/$',views.sincro_familia),
    url(r'^api/sincro_encuestado/$',views.sincro_encuestado),
    url(r'^api/sincro_agroquimico/$',views.sincro_agroquimico),
    url(r'^api/sincro_encuesta/$',views.sincro_encuesta),
    url(r'^api/sincro_invernaculo/$',views.sincro_invernaculo),
    url(r'^api/sincro_cultivo/$',views.sincro_cultivo),
    url(r'^api/sincro_agroquimico_usado/$',views.sincro_agroquimico_usado),
    url(r'^api/get_ids_by_transaccion/(?P<transaccion>[0-9A-Za-z-]+)/$',views.get_ids_by_transaccion),
]
