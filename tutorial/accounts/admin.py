from django.contrib import admin
from  . models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_info', 'city', 'phone', 'website')

    # user_info is the description

    def user_info(self, obj):
        return obj.description


admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.site_header = "Administration "

