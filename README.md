# django web developement
1. [Creating django project](#Creating-django-project)    
1. [Creating django app](#Creating-django-app)  
1. [Django Template](#Django-Template)  
1. [Static file](#Static-file)  
1. [Django template language use and example](#Django-template-language-use-and-example)  
1. [How to build a login form using django login module](#How-to-build-a-login-form-using-django-login-module)  
1. [How to use super user and migrations](#How-to-use-super-user-and-migrations) 
1. [How to use database backend and migrations](#How-to-use-database-backend-and-migrations)  
1. [use of signal](#use-of-signal)   
1. [Create user register using django model UserCreationForm](#Create-user-register-using-django-model-UserCreationForm)  
1. [Custom Create user register using django model UserCreationForm ](#Custom-Create-user-register-using-django-model-UserCreationForm ) 
1. [how to extract data from django use](#how-to-extract-data-from-django-use)  
1. [Edit user data using django model UserChangeForm](#Edit-user-data-using-django-model-UserChangeForm)  
1. [custom Edit user data using django model UserChangeForm](#custom-Edit-user-data-using-django-model-UserChangeForm)  
1. [Change password After login the admin using django model PasswordChangeForm,update_session_auth_hash](#Change-password-After-login-the-admin-using-django-model-PasswordChangeForm,update_session_auth_hash)  
1. Change password when user forget password using django model password_reset, password_reset_done, password_reset_confirm, password_reset_complete  
1. user authenticated using template in html or login_required decorator  
1. [middleware](#middleware)  
1. [Namespace](#Namespace)  
1. [Basic question](#Basic-question)
1. [Intermediate question](#Intermediate-question )

## Full details 
1. [Creating django project](https://github.com/MaazMS/django-web-developement/blob/Django/Document/1.md)    
1. [Creating django app](https://github.com/MaazMS/django-web-developement/blob/Django/Document/2.md)  
    a. How to install django app  
    a. Setup of url Configuration, Root url and views. 
1. [Django Template](https://github.com/MaazMS/django-web-developement/blob/Django/Document/3.md)     
    a. What is Django Templates?       
    b. Why Django Template?   
    c. Structure of template.    
    d. Advance structure of template.    
    c. How to map templates.   
1. [Static file](https://github.com/MaazMS/django-web-developement/blob/Django/Document/4.md) 
    a. Structure of static file.   
    b. Load static file.   
    c. How to link static file.   
1. [Django template language](https://github.com/MaazMS/django-web-developement/blob/Django/Document/5.md)  
    a. How to pass variable data from view to html.  
    b. How to  pass list and access using loop.  
    c. How to apply filters on variable using pipe **|**  
    d. How to use comment in template.  
    e. Template inheritance. 
1. [How to build a login form using django login module](https://github.com/MaazMS/django-web-developement/blob/Django/Document/6.md)    
    a. from django.contrib.auth.views import login     
    b. Use login module.      
    c. How to use template. hit {'template_name': 'file_name.html'}    
    d. login redirect `/accounts/profile` to change by default location.    
1. [How to use super user and migrations ](https://github.com/MaazMS/django-web-developement/blob/Django/Document/7.md)     
    a. What are tables inside django project by default.     
    b. When create django super user.      
1. [How to use database backend and migrations](https://github.com/MaazMS/django-web-developement/blob/Django/Document/8.md)     
    a. create model and register model name  
    b. After and before makemigrations for database.     
    c. After and before migrate for database   
1. [use of signal](https://github.com/MaazMS/django-web-developement/blob/Django/Document/9.md)     
    a. What is signal    
    b. Sender and receiver   
    c. Example    
1. [Create user register using django model UserCreationForm](https://github.com/MaazMS/django-web-developement/blob/Django/Document/10.md)  
    a. from django.contrib.auth.forms import UserCreationForm   
    b. Code with explain for user register in `app_name/views.py`        
    c. form in html page.   
1. [Custom Create user register using django model UserCreationForm](https://github.com/MaazMS/django-web-developement/blob/Django/Document/11.md)    
    a. from django import forms    
    b. from django.contrib.auth.models import User    
    c. from django.contrib.auth.forms import UserCreationForm   
    b. Code with explain for user register in `app_name/forms.py`     
    e. form in html page.
    f. views.py code.   
    g. Hit custom register and django default register at time one is show.     
1. [how to extract data from django user](https://github.com/MaazMS/django-web-developement/blob/Django/Document/12.md)    
    a. user is User model object.  
    b. code with explain.           
    c. form in html page hit {{ user.attribute_name}}     
1. [Edit user data using django model UserChangeForm](https://github.com/MaazMS/django-web-developement/blob/Django/Document/13.md)     
    a. from django.contrib.auth.forms import UserChangeForm     
    b. Code with explain for Edit user data in `app_name/views.py`     
    c. form in html page.     
    e. views.py code    
1. [custom Edit user data using django model UserChangeForm](https://github.com/MaazMS/django-web-developement/blob/Django/Document/14.md)      
    a. from django import forms      
    b. from django.contrib.auth.models import User    
    c. from django.contrib.auth.forms import UserChangeForm   
    d. Code with explain for Edit user data in `app_name/forms.py`  
    e. form in html page. 
    f. views.py code.      
    g. Hit custom register and django default register at time one is show.      
1. [Change password After login the admin using django model PasswordChangeForm,update_session_auth_hash ](https://github.com/MaazMS/django-web-developement/blob/Django/Document/15.md)      
    a. from django.contrib.auth.forms import PasswordChangeForm  
    b. code with explain for change password in `app_name/views.py`  
    c. form in html  
    d. if view user profile it show anonymous user. solve by `update_session_auth_hash`     
    f. from django.contrib.auth import update_session_auth_hash   
1. [Change password when user forget password using django model password_reset, password_reset_done, password_reset_confirm, password_reset_complete](https://github.com/MaazMS/django-web-developement/blob/Django/Document/16.md)     
    a. from django.contrib.auth.views import password_reset after error    
    b. from django.contrib.auth.views import password_reset_done after error  
    c. from django.contrib.auth.views import password_reset_confirm after error   
    d. from django.contrib.auth.views import password_reset_complete after solve   
    e. All code is writen in `app_name/urls.py`   
1. [user authenticated using template in html or login_required decorator.](https://github.com/MaazMS/django-web-developement/blob/Django/Document/17.md)     
    a. {% if user.is_authenticated %}   
    b. from django.contrib.auth.decorators import login_required 
    c. @login_required   
1. [middleware](https://github.com/MaazMS/django-web-developement/blob/Django/Document/18.md)      
    a. What is middleware      
    b. "Common” middleware hit (Forbids access, URL rewriting slash ,PREPEND_WWW, Sets the Content-Length )       
    c. CsrfViewMiddleware hit (adding hidden form fields to POST forms and checking requests for the correct value).  
    d. SessionMiddleware hit(Enables session support.)    
    e. AuthenticationMiddleware hit(representing the currently-logged-in user, Adds the user attribute)    
    f. MessageMiddleware hit (Enables cookie- and session-based message support)      
    g. XFrameOptionsMiddleware hit (Clickjacking User Interface redress, UI redress, UI redressing attack for tricking a user)   

1. [Custom LoginRequiredMiddleware](https://github.com/MaazMS/django-web-developement/blob/Django/Document/19.md)    
    a. add settings.py middleware hit ('tutorial.middleware.LoginRequiredMiddleware' )    
    b. from django.conf import settings   
    d. 'LoginRequiredMiddleware' object is not callable    
    e. No need @login_required decorator.  hit (AnonymousUser)    
    f. login redirect define (hit change setting  LOGIN_URL = '/accounts/login/' )     
    g. Allow to access some url (hit LOGIN_EXEMPT_URLS = ( r'^accounts/register/$', r'^accounts/logout/$' ))      
    h. process_view()     
    i. what is the use of process_view()      
    j. How to avoid head code url hit ( settings.py LOGIN_URL = '/accounts/login/') `reverse` function    
1. [Namespace](https://github.com/MaazMS/django-web-developement/blob/Django/Document/20.md)      
    a. What is the namespace?   
    b. create namespace `project_name/urls.py` hit`url(r'^accounts/', include('accounts.urls', namespace='accounts')`    
    c. Avoid confuse.  
    d. use namespace in html page `<a href="{% url 'accounts :view_profile' %}">`  
    e. `reverse `  function unse namespace.    
1. [Upload and display static files](https://github.com/MaazMS/django-web-developement/blob/Django/Document/upload_images_21.md)      
    a. Add image column in model. hit `models.ImageField(upload_to='profile_images', blank=True)`     
    b. Settings.py  add `MEDIA_URL = '/media/'`     
    c. when image upload then automatically folder create in app and image store. hit `pload_to='profile_images'`        
    d. saving files uploaded by use during development `project_name/urls.py`     
    e. show images using template hit ` <img src="{{ user.userprofile.image.url }}" width="240">`         

1. [Basic question](https://github.com/MaazMS/django-web-developement/blob/Django/Document/28.md)
    1. Which architectural pattern does Django follow?  
    1. What are Models?  
    1. What are views?  
    1. Is Django a CMS?   
    1. What are the features available in Django web framework?      
1. [Intermediate question](https://github.com/MaazMS/django-web-developement/blob/Django/Document/29.md)  
    1. What is Django ORM?   
    1. What is Django Session?   
    1. What is the role of Cookie in Django?   
          