from django.conf.urls import url
from .views import UserListView

app_name = "api"

urlpatterns = [
    url(r'^user/', UserListView.as_view(), name='user-list-view')
]