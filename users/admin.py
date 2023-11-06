from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    """Custom user admin"""
    list_display = ['last_name','first_name','email','username','currency','gender','superhost','is_active']
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile", {
                "fields": (
                    "bio", "avatar","gender","date_of_birth","languages","currency","superhost"
                )
            }
        ),
    )

# Register the User model with your custom admin class
admin.site.register(User, CustomUserAdmin)
