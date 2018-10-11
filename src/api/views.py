# Importing User Model
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Post

# Serializer and API View
from .serializers import UserSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
# Essentials for Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from .pagination import (
    PostLimitOffsetPagination,
    PostPageNumberPagination
)

from .permissions import IsOwnerOrReadOnly

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

class CurrentUserView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    lookup_field = "id"

class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permision_classes = (IsAuthenticated, )
    lookup_field = "id"

class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    lookup_field = "id"

class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    lookup_field = "id"

    # Fills the data automatically from author
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user, title="my title")

class PostRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    lookup_field = "id"


class PostOverridingListView(ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, *args, **kwargs):
        posts = Post.objects.all()
        return posts.filter(title__startswith="G") 

class PostQuerySetView(ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    # Query Set using GET
    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q") or None
        if query is None:
            return queryset_list
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) 
            # Q(author__first_name__icontains=query) |
            # Q(author__last_name__icontains=query) 
            # Q(author__username__icontains=query)
        ).distinct()
        return queryset_list

class PostSearchFilterView(ListAPIView):
    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication
    )
    permission_classes = (
        IsAuthenticated,
    )
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        'title', 
        'description', 
        'author__first_name', 
        'author__last_name', 
        'author__username'
    ]
    # http://localhost:8000/api/v1/posts-search-filter/?search=a&q=g&ordering=title
    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get('q') or None
        if query is None:
            return queryset_list
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ) 
        return queryset_list

class PostLimitOffsetView(ListAPIView):
    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication
    )
    permission_classes = (
        IsAuthenticated,
    )
    # http://localhost:8000/api/v1/posts/?limit=1&offset=1
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostLimitOffsetPagination

class PostPagePaginationView(ListAPIView):
    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication
    )
    permission_classes = (
        IsAuthenticated,
    )
    # http://localhost:8000/api/v1/posts/?limit=1&offset=1
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPageNumberPagination
