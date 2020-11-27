from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    login ,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,

)


urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^welcome/', views.welcome),
    url(r'value/', views.passing_value),
    url(r'override/', views.override),
    url(r'^login/',login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/',logout, {'template_name': 'accounts/logout.html'}),
    # url(r'register/', views.register),
    # url(r'^custom_register/', views.custom_register),
    url(r'^user_profile/', views.user_profile),
    # url(r'^edit_user_profile/', views.edit_user_profile),
    # url(r'^edit_personal_info/', views.Edit_personal_info),
    url(r'^change_password/', views.change_password, name='change_password'),
    url(r'^reset-password/', password_reset, name='password_reset'),
    url(r'^reset-password/done/', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/    (?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/', password_reset_complete, name='password_reset_complete'),
]

"""" 
reset-password/
NoReverseMatch at /accounts/reset-password
Reverse for 'password_reset_done' with arguments '()' and keyword arguments '{}' not found. 0 pattern(s) tried: []
reset-password/done/
NoReverseMatch at /accounts/reset-password/
Reverse for 'password_reset_confirm' with arguments '()' and keyword arguments '{'uidb64': b'MQ', 'token': '5ly-13ade6f390cf48080cec'}' not found. 0 pattern(s) tried: []
reset-password/confirm/ 
Reverse for 'password_reset_confirm' with arguments '()' and keyword arguments '{'uidb64': b'MQ', 'token': '5ly-13ade6f390cf48080cec'}' not found. 1 pattern(s) tried: ['accounts/reset-password/confirm/']
particular user change password use token (accept two variable )   
r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$'
ConnectionRefusedError at /accounts/reset-password/ 

Sending emails from Django during development without using a real SMTP server. Python comes with a very basic and integrated SMTP server. To start it just open a terminal and type: python -m smtpd -n -c DebuggingServer localhost:1025 Then configure your settings.py
settings.py file buttom add  
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
"""