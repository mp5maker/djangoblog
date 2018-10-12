from django.contrib.auth.models import User
from .models import Post
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError,
)

# USER SERIALIZER [MODEL SERIALIZER :: REST FRAMEWORK]
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

# POST SERIALIZER [MODEL SERIALIZER :: REST FRAMEWORK]
class PostSerializer(ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'description'
        )

# POST SERIALIZER [HYPERLINKED IDENTITY FIELD  :: REST FRAMEWORK]
delete_url = HyperlinkedIdentityField(
    view_name="api:post-delete-view",
    lookup_field="id"
)

class PostHyperlinkedIdentitySerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api:post-detail-view',
        lookup_field='id'
    )
    delete_url = delete_url
    author = UserSerializer()
    class Meta:
        model = Post
        fields = (
            'url',
            'id',
            'author',
            'title',
            'description',
            'delete_url',
        )

# POST SERIALIZER [HYPERLINKED METHOD FIELD  :: REST FRAMEWORK]
class PostMethodFieldSerializer(ModelSerializer):
    author = SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'description',
        )
    
    def get_author(self, obj):
        return str(obj.author.username)

class PostReadOnlyFieldSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description'
        )
        read_only_fields = [
            'description',
        ]

class PostValidationSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description'
        )
    # Validation
    def validate_title(self, title):
        if title == 'abc':
            raise ValidationError("Not a valid title")
        return title