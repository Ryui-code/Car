from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Comment, Car

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'phone_number', 'profile_picture', 'status')
        }),
    )

admin.site.register(Comment)
admin.site.register(Car)