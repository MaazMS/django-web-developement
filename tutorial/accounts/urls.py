from django.conf.urls import url
from . import views
from django.contrib.auth.views import login , logout


urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^welcome/', views.welcome),
    url(r'value/', views.passing_value),
    url(r'override/', views.override),
    url(r'^login/',login, {'template_name': 'accounts/login.html'}),
    url(r'^logout/',logout, {'template_name': 'accounts/logout.html'}),
    # url(r'register/', views.register),
    # url(r'^custom_register/', views.custom_register),
    # url(r'^user_profile', views.user_profile),
    # url(r'^edit_user_profile', views.edit_user_profile),
    # url(r'^edit_personal_info', views.Edit_personal_info),
    url(r'^change_password', views.change_password, name='change_password'),
]