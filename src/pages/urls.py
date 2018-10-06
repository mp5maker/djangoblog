from django.conf.urls import url
from .views import LandingPage

app_name = 'pages'

urlpatterns = [
    url(r'^$', LandingPage.as_view(), name='landing-page')
]