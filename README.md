# django web developement
1. [Creating django project](https://github.com/MaazMS/django-web-developement/blob/Django/Document/1.md)    
2. [Creating django app](https://github.com/MaazMS/django-web-developement/blob/Django/Document/2.md)  
    a. How to install django app  
    a. Setup of url Configuration, Root url and views. 
3. [Django Template](https://github.com/MaazMS/django-web-developement/blob/Django/Document/3.md)     
    a. What is Django Templates?       
    b. Why Django Template?   
    c. Structure of template.    
    d. Advance structure of template.    
    c. How to map templates.   
4. [Static file](https://github.com/MaazMS/django-web-developement/blob/Django/Document/4.md) 
    a. Structure of static file.   
    b. Load static file.   
    c. How to link static file.   
 5. [Django template language](https://github.com/MaazMS/django-web-developement/blob/Django/Document/5.md)  
    a. How to pass variable data from view to html.  
    b. How to  pass list and access using loop.  
    c. How to apply filters on variable using pipe **|**  
    d. How to use comment in template.  
    e. Template inheritance. 
6. [How to build a login form using django login module](https://github.com/MaazMS/django-web-developement/blob/Django/Document/6.md)    
    a. from django.contrib.auth.views import login     
    b. Use login module.      
    c. How to use template. hit {'template_name': 'file_name.html'}    
    d. login redirect `/accounts/profile` to change by default location.    
7. [How to use super user and migrations ](https://github.com/MaazMS/django-web-developement/blob/Django/Document/7.md)     
    a. What are tables inside django project by default.     
    b. When create django super user.      
8. [How to use database backend and migrations](https://github.com/MaazMS/django-web-developement/blob/Django/Document/8.md)     
    a. create model and register model name  
    b. After and before makemigrations for database.     
    c. After and before migrate for database   
9. [use of signal](https://github.com/MaazMS/django-web-developement/blob/Django/Document/9.md)     
    a. What is signal    
    b. Sender and receiver   
    c. Example    
10. [Create user register using django model UserCreationForm](https://github.com/MaazMS/django-web-developement/blob/Django/Document/10.md)  
    a. from django.contrib.auth.forms import UserCreationForm   
    b. Code with explain for user register in `app_name/views.py`        
    c. form in html page.   
11. [Custom Create user register using django model UserCreationForm](https://github.com/MaazMS/django-web-developement/blob/Django/Document/11.md)    
    a. from django import forms    
    b. from django.contrib.auth.models import User    
    c. from django.contrib.auth.forms import UserCreationForm   
    b. Code with explain for user register in `app_name/forms.py`     
    e. form in html page.
    f. views.py code.   
    g. Hit custom register and django default register at time one is show.     
12. [how to extract data from django user](https://github.com/MaazMS/django-web-developement/blob/Django/Document/12.md)    
    a. user is User model object.  
    b. code with explain.           
    c. form in html page hit {{ user.attribute_name}}     
13. [Edit user data using django model UserChangeForm](https://github.com/MaazMS/django-web-developement/blob/Django/Document/13.md)     
    a. from django.contrib.auth.forms import UserChangeForm     
    b. Code with explain for Edit user data in `app_name/views.py`     
    c. form in html page.     
    e. views.py code    
14. [custom Edit user data using django model UserChangeForm](https://github.com/MaazMS/django-web-developement/blob/Django/Document/14.md)      
    a. from django import forms      
    b. from django.contrib.auth.models import User    
    c. from django.contrib.auth.forms import UserChangeForm   
    d. Code with explain for Edit user data in `app_name/forms.py`  
    e. form in html page. 
    f. views.py code.      
    g. Hit custom register and django default register at time one is show.      
15. [Change password After login the admin using django model PasswordChangeForm,update_session_auth_hash ](https://github.com/MaazMS/django-web-developement/blob/Django/Document/15.md)      
    a. from django.contrib.auth.forms import PasswordChangeForm  
    b. code with explain for change password in `app_name/views.py`  
    c. form in html  
    d. if view user profile it show anonymous user. solve by `update_session_auth_hash`     
    f. from django.contrib.auth import update_session_auth_hash   
16. [Change password when user forget password using django model password_reset, password_reset_done, password_reset_confirm, password_reset_complete](https://github.com/MaazMS/django-web-developement/blob/Django/Document/16.md)     
    a. from django.contrib.auth.views import password_reset after error    
    b. from django.contrib.auth.views import password_reset_done after error  
    c. from django.contrib.auth.views import password_reset_confirm after error   
    d. from django.contrib.auth.views import password_reset_complete after solve   
    e. All code is writen in `app_name/urls.py`   
17. [user authenticated using template in html or login_required decorator.](https://github.com/MaazMS/django-web-developement/blob/Django/Document/17.md)     
    a. {% if user.is_authenticated %}   
    b. from django.contrib.auth.decorators import login_required 
    c. @login_required   
18. [middleware](https://github.com/MaazMS/django-web-developement/blob/Django/Document/18.md)      
    a. What is middleware      
    b. "Common” middleware hit (Forbids access, URL rewriting slash ,PREPEND_WWW, Sets the Content-Length )       
    c. CsrfViewMiddleware hit (adding hidden form fields to POST forms and checking requests for the correct value).  
    d. SessionMiddleware hit(Enables session support.)    
    e. AuthenticationMiddleware hit(representing the currently-logged-in user, Adds the user attribute)    
    f. MessageMiddleware hit (Enables cookie- and session-based message support)      
    g. XFrameOptionsMiddleware hit (Clickjacking User Interface redress, UI redress, UI redressing attack for tricking a user)   

19. [Custom LoginRequiredMiddleware](https://github.com/MaazMS/django-web-developement/blob/Django/Document/19.md)    
    a. add settings.py middleware hit ('tutorial.middleware.LoginRequiredMiddleware' )    
    b. from django.conf import settings   
    d. 'LoginRequiredMiddleware' object is not callable    
    e. No need @login_required decorator.  hit (AnonymousUser)    
    f. login redirect define (hit change setting  LOGIN_URL = '/accounts/login/' )     
    g. Allow to access some url (hit LOGIN_EXEMPT_URLS = ( r'^accounts/register/$', r'^accounts/logout/$' ))      
    h. process_view()     
    i. what is the use of process_view()      
    j. How to avoid head code url hit ( settings.py LOGIN_URL = '/accounts/login/') `reverse` function    
20. [Namespace](https://github.com/MaazMS/django-web-developement/blob/Django/Document/20.md)      
    a. What is the namespace?   
    b. create namespace `project_name/urls.py` hit`url(r'^accounts/', include('accounts.urls', namespace='accounts')`    
    c. Avoid confuse.  
    d. use namespace in html page `<a href="{% url 'accounts :view_profile' %}">`  
    e. `reverse `  function unse namespace.    
21. [Upload and display static files](https://github.com/MaazMS/django-web-developement/blob/Django/Document/upload_images_21.md)      
    a. Add image column in model. hit `models.ImageField(upload_to='profile_images', blank=True)`     
    b. Settings.py  add `MEDIA_URL = '/media/'`     
    c. when image upload then automatically folder create in app and image store. hit `pload_to='profile_images'`        
    d. saving files uploaded by use during development `project_name/urls.py`     
    e. show images using template hit ` <img src="{{ user.userprofile.image.url }}" width="240">`         
        
           
`https://stackoverflow.com/questions/50486207/how-to-use-while-loop-in-django-template`    
   