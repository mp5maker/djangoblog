from django.contrib.auth.models import User
from .models import Post
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'last_login',
            'password',
            'is_superuser',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
        )

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description'
        )