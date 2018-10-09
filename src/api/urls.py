from django.conf.urls import url, include
from .views import UserListView, PostListView, CurrentUserView

app_name = "api"

urlpatterns = [
    url(r'rest-auth/', include('rest_auth.urls')),
    url(r'^users/', UserListView.as_view(), name='user-list-view'),
    url(r'^posts/', PostListView.as_view(), name='post-list-view'),
    url(r'^current-user/', CurrentUserView.as_view(), name='current-user-view'),
]
