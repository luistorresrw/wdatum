from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from principal import views
from rest_framework.authtoken import views as token_views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupviewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('principal.urls')),
    url(r'^api/',include(router.urls)),
    #url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    #url(r'^api-token-auth/', token_views.obtain_auth_token),
    url(r'^api/auth/', include('rest_auth.urls')),
]
