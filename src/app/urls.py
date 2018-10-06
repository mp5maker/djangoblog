from django.conf.urls import url
from .views import LandingPage

app_name = 'app'

urlpatterns = [
    url(r'^$', LandingPage.as_view(), name='landing-page')
]