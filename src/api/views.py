from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer