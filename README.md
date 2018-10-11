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

## How the authentication works ##
> Do no memorize just learn the concept flow

**Working in shell**
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

**Adding Rest Framework Authorization Token**

settings.py
```bash
INSTALLED_APPS = [
    'rest_framework.authtoken',
    'rest_auth'
    ...
]
```

```bash
python manage.py migrate
```

settings.py
```bash
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', )
}
```
# Essentials for Authentication
```python
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
```

## Django Rest Authentication ##
```bash
pip install django-rest-auth
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
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', 
        'rest_framework.permissions.IsAdminUser'
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 1,
}
```

## Rest Framework ##
**Serializers**
1. from *rest_framework.serializers* import (
    **ModelSerializer,
    HyperlinkedIdentityField,
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

**Permissions**
1. from *rest_framework.permissions* import **BasePermission**

**Pagination**
1. from *rest_framework.pagination* import(
    **LimitOffsetPagination,
    PageNumberPagination**
)