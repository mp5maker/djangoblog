## Creating Django Blog with Rest Framework ##
> *If this installation is hard for you please go to my library to learn about npm*

> *Go to my **trydjango** repository and visit to [Coding Entreprenuers](https://www.codingforentrepreneurs.com/)* **Check their youtube channels too**

> *Go to my **library** repository and visit to traversy media to build a foundation on npm and javascript libraries* [Traversy Media](http://traversymedia.com/) **Check their youtube channels too**

**Installation**
1. Pip
2. Python v36-32
3. Node/Npm
4. virtualenv, virtualenvwrapper

```bash
mkdir src
mkvirtualenv djangoblog
touch requirements.txt
pip install freeze
```

requirements.txt
```txt
Django==1.11
djangorestframework==3.7.7
```

```bash
pip install -r requirements.txt
cd src
django-admin startproject settings .
python maange.py startapp pages
```

**Requirements**
1. Django 1.11
2. Django Rest Framework
3. Virtual Environment

**Front End Modules**
1. Angular JS
2. Bootstrap
3. Materialize
4. Sass
5. jQuery
6. Popper
7. Gulp

```bash
npm init -y
npm install bootstrap jquery popper.js angular angular-ui-router angular-animate font-awesome
npm install --save-dev gulp gulp-sass gulp-concat
```

> Good Luck Learning! :D :D

## Authentication ##
1) Check in settings.py
2) *django.contrib.auth*
3) Using str(Model.query), dir(Model), Model._meta.get_fields()

```bash
from django.contrib.auth.models import User

# Gives all the methods and attributes associeated with User
dir(User)

# Gives list of field names
User._meta.get_fields() 
```

**Creating a User**
```bash
user = User.objects.create_user('login', 'email@hotmail.com', 'password')
user.save()
```

**Authentication**
```bash
from django.contrib.auth import authenticate
user = authenticate(username="login", password="password")
if user is not None:
    print("This user exists")
else:
    print("Invalid User")
```
## Rest Framework ##
**Authentication and Filter Setup**
```bash
pip install django-rest-auth
pip install django-filter
```
settings.py
```python
INSTALLED_APPS = [
    # Django Api
    'api',

    # Django Apps
    'app',

    # Django Rest Framework
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',


    # Default Setting From Django Frame Work
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Extra Django 
    'django.contrib.admindocs'
]

REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # Permission
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', 
        'rest_framework.permissions.IsAdminUser'
    ),
    # Filter
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # Pagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 1,
}
```

```bash
# For rest_framework.authtoken
python manage.py migrate
```

***

**Serializers**
1. from *rest_framework.serializers* import (
    **ModelSerializer,
    HyperlinkedIdentityField,
    ValidationError,
    SerializerMethodField**
    )

**Views**
1. from *rest_framework.views* import **APIView**

2. from *rest_framework.generics* (
    **ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView**
    )

3. from *rest_framework.authentication* import (
    **SessionAuthentication,
    BasicAuthentication**
    )

4. from *rest_framework.filters* import (
    **SearchFilter,
    OrderingFilter**
    )

5. from *rest_framework.permissions* import (
    **AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,**
    )

6. from *rest_framework.permissions* import (
    **AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,**
    )

7. from *rest_framework.mixins* import (
    **ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin**
    )

**Permissions**
1. from *rest_framework.permissions* import **BasePermission**

**Pagination**
1. from *rest_framework.pagination* import(
    **LimitOffsetPagination,
    PageNumberPagination**
)
***

**Serializer**
```python
## Typically we do that with the model with Foreign Key
inheritance_field = SomeOtherSerializer()

## Inside **Class Meta**
model = SomeModel
fields = (
    'title',
    'description',
    'some_field',
    'inheritance_field',
    'url'
)
read_only_fields = [
    'title',
    'description'
]
extra_kwargs = {
    "password" : {
        "write_only": true
    }
}
```

**Serializer Modifier**
```python
1. SerializerMethodField() 
    def get_some_field(self, obj):

2. HyperlinkedIdentityField()
    url = HyperlinkedIdentityField(
        view_name='api:post-detail-view',
        lookup_field='id'
    )
```

***

**View**
```python
1. queryset 
2. serializer_class
3. authentication_classes 
4. permission_classes 
5. pagination_classes
```

**Views Modifiers**
```python
1. def get_queryset(self, *args, **kwargs):
2. def get(self, *args, **kwargs):
2. def post(self, *args, **kwargs):
3. def put(self, *args, **kwargs):
3. def patch(self, *args, **kwargs):
4. def delete(self, *args, **kwargs):
5. def create(self, *args, **kwargs)"
```

**Mixins**
```python
1. self.list(request, *args, **kwargs)
2. self.retrieve(request, *args, **kwargs)
3. self.create(request, *args, **kwargs)
4. self.update(request, *args, **kwargs)
5. self.destroy(request, *args, **kwargs)
```

***

**Persmission**
```python
# BASE PERMISSION
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in self.my_safe_method:
            return True
        return obj.author == request.user
```

**Pagination**
```python
# POST [LIMITOFFSETPAGINATION :: REST FRAMEWORK]
class PostLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 2

# POST [PAGENUMBERPAGINATION :: REST FRAMEWORK]
class PostPageNumberPagination(PageNumberPagination):
    page_size = 2
```

***

## Login System Using Rest Framework ##