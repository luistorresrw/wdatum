from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from principal import views
from rest_framework.authtoken import views as token_views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupviewSet)
router.register(r'updates',views.UpdateViewSet)
router.register(r'sincro_establecimiento',views.EstablecimientoViewSet)
router.register(r'regimen_tenencia',views.RegimenTenenciaViewSet)
router.register(r'sincro_encuestado',views.EncuestadoViewSet)
router.register(r'sincro_familia',views.FamiliaViewSet)
router.register(r'sincro_agroquimicos',views.AgroquimicoViewSet)
router.register(r'nacionalidad',views.NacionalidadViewSet)
router.register(r'nivel_instrucion',views.NivelInstruccionViewSet)
router.register(r'factor_climatico',views.FactorClimaticoViewSet)
router.register(r'triple_lavado',views.TripleLavadoViewSet)
router.register(r'asesoramiento',views.AsesoramientoViewSet)
router.register(r'sincro_encuesta',views.EncuestaViewSet)
router.register(r'sincro_invernaculos',views.InvernaculoViewSet)
router.register(r'material_estructura',views.MaterialEstructuraViewSet)
router.register(r'anio_construccion',views.AnioConstruccionViewSet)
router.register(r'sincro_cultivos',views.CultivosViewSet)
router.register(r'especie',views.EspecieViewSet)
router.register(r'tipo_cultivo',views.TipoCultivoViewSet)
router.register(r'tipo_produccion',views.TipoProduccionViewSet)
router.register(r'eleccion_cultivo',views.EleccionCultivoViewSet)
router.register(r'sincro_agroquimico_usado',views.AgroquimicoUsadoViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('principal.urls')),
    url(r'^api/',include(router.urls)),
    #url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    #url(r'^api-token-auth/', token_views.obtain_auth_token),
    url(r'^api/auth/', include('rest_auth.urls')),
    url(r'^api/actualizaciones_posteriores_a/(?P<last_update>[0-9]+)/$',views.UpdatesPosteriores),
    url(r'^api/last_update/$',views.lastUpdate),

]
