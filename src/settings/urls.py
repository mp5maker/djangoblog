from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'rest-auth/', include('rest_auth.urls')),
    url(r'^', include('app.urls')),
    url(r'^api/v1/', include('api.urls')),
]
