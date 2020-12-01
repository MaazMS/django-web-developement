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
    url(r'^$', views.welcome),
    url(r'^welcome/', views.welcome),
    url(r'value/', views.passing_value),
    url(r'override/', views.override),
    url(r'^login/',login, {'template_name': 'accounts/login.html'}, name= 'login'),
    url(r'^logout/',logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'register/', views.register),
    url(r'^custom_register/', views.custom_register),
    url(r'^user_profile/', views.user_profile),
    url(r'^edit_user_profile/', views.edit_user_profile),
    url(r'^edit_personal_info/', views.Edit_personal_info),
    url(r'^change_password/', views.change_password, name='change_password'),
    url(r'^reset-password/', password_reset, name='password_reset'),
    url(r'^reset-password/done/', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/    (?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/', password_reset_complete, name='password_reset_complete'),

]
