from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('app.urls')),
    url(r'^api/v1/', include('api.urls')),
]
