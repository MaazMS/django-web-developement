# django-web-developement
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
       
`https://stackoverflow.com/questions/50486207/how-to-use-while-loop-in-django-template`
8. custom login page `https://overiq.com/django-1-10/django-logging-users-in-and-out/`     