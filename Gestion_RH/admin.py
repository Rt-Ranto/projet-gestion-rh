from django.contrib import admin
from django.utils.html import format_html
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff','avatar')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Infos personnelles', {'fields': ('first_name', 'last_name', 'email', 'photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    def avatar(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%;" />',
                obj.photo.url
            )
            return "_"
        
    avatar.short_description = "Photo"