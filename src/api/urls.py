from django.conf.urls import url, include
from .views import (
    UserListView, 
    CurrentUserView,
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
    PostRetrieveUpdateView,
    PostOverridingListView
)

app_name = "api"

urlpatterns = [
    url(r'rest-auth/', include('rest_auth.urls')),
    url(r'^users/$', UserListView.as_view(), name='user-list-view'),
    url(r'^current-user/', CurrentUserView.as_view(), name='current-user-view'),
    url(r'^posts/$', PostListView.as_view(), name='post-list-view'),
    url(r'^posts/(?P<id>[0-9]+)$', PostDetailView.as_view(), name='post-detail-view'),
    url(r'^posts/edit/(?P<id>[0-9]+)$', PostUpdateView.as_view() , name="post-edit-view"),
    url(r'^posts/delete/(?P<id>[0-9]+)$', PostDeleteView.as_view(), name="post-delete-view"),
    url(r'^posts/create/$', PostCreateView.as_view(), name="post-create-view"),
    url(r'^posts/update/(?P<id>[0-9]+)$', PostRetrieveUpdateView.as_view() , name="post-update-view"),
    url(r'^posts-override/$', PostOverridingListView.as_view(), name='post-overriding-list-view'),
]
