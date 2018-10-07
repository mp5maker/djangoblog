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

**Urls Provided by Django Default Authentication**
```bash
login/ [name='login']
logout/ [name='logout']
password_change/ [name='password_change']
password_change/done/ [name='password_change_done']
password_reset/ [name='password_reset']
password_reset/done/ [name='password_reset_done']
reset/<uidb64>/<token>/ [name='password_reset_confirm']
reset/done/ [name='password_reset_complete']
```