from django.contrib import admin

# Register your models here.
from home.models import Setting, Contact, UserProfile


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'status']
    list_filter = ['status']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'city', 'image_tag']

admin.site.register(Setting)
admin.site.register(Contact, ContactAdmin)
admin.site.register(UserProfile, UserProfileAdmin)