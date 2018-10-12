# Importing User Model
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Post

# Serializer and API View
from .serializers import (
    UserSerializer, 
    PostSerializer,
    PostHyperlinkedIdentitySerializer,
    PostMethodFieldSerializer,
    PostReadOnlyFieldSerializer,
    PostValidationSerializer
)
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

from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)

# USER LIST [READ]
class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

# CURRENT USER [DETAIL]
class CurrentUserView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# POST [LIST]
class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

# POST [DETAIL]
class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    lookup_field = "id"

# POST [UPDATE]
class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permision_classes = (IsAuthenticated, )
    lookup_field = "id"

# POST [DESTROY]
class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    lookup_field = "id"

# POST [CREATE]
class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    lookup_field = "id"

    # Fills the data automatically from author
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user, title="my title")

# POST [READ & UPDATE]
class PostRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    lookup_field = "id"

# POST [FILTER]
class PostOverridingListView(ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self, *args, **kwargs):
        posts = Post.objects.all()
        return posts.filter(title__startswith="G") 

# POST [Q FILTER :: DJANGO BUILT-IN]
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

# POST [SEARCH FILTER, ORDER FILTER :: REST FRAMEWORK]
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

# POST [LIMITOFFSETPAGINATION :: REST FRAMEWORK]
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

# POST [PAGENUMBERPAGINATION :: REST FRAMEWORK]
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

# POST [HYPERLINKIDENTITYFIELD :: REST FRAMEWORK]
class PostHyperlinkedIdentityView(ListAPIView):
    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication
    )
    permission_classes = (
        IsAuthenticated,
    )
    queryset = Post.objects.all()
    serializer_class = PostHyperlinkedIdentitySerializer

# POST [SerializerMethodField :: REST FRAMEWORK]
class PostMethodFieldView(ListAPIView):
    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication
    )
    permission_classes = (
        IsAuthenticated,
    )
    queryset = Post.objects.all()
    serializer_class = PostMethodFieldSerializer

# POST [ModelMixins :: REST FRAMEWORK]
class PostEditDeleteMixinView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# POST [READONLYFIELDS :: REST FRAMEWORK]
class PostReadOnlyFieldView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostReadOnlyFieldSerializer
    lookup_field = "id"
    authentication_classes = (
        SessionAuthentication,
        BasicAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )


class PostValidationView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostValidationSerializer
    authentication_classes = (
        BasicAuthentication,
        SessionAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )