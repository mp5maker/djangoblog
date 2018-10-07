# Importing User Model
from django.contrib.auth.models import User

# Serializer and API View
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView

# Essentials for Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )