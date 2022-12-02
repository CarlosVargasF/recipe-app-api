"""
django admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# good practice in case site translation feature is neede in future  
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users"""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = ( # defines the sections showed in admin page
        (None,
        {'fields': (
            'email',
            'password',
            )
        }),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            _('Important dates'),
            {
                'fields': (
                    'last_login',        
                )
            }
        )
    )
    
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',), # optional, CSS stuff
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )

        }),
    )

# REGISTER MODELS
# /!\ 2nd optional arg needed to consider the custom class
admin.site.register(models.User, UserAdmin) 
admin.site.register(models.Recipe)
admin.site.register(models.Tag)
admin.site.register(models.Ingredient)
