from django.contrib import admin
from  . models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'city', 'phone', 'website')

    def user_info(self, obj):
        return obj.description
    user_info.short_description =  'info'

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset =queryset.order_by('-phone')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.site_header = "Administration "

