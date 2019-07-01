from django.contrib import admin
from django.db import models
from .models import HomePage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _


# Define a new FlatPageAdmin
class MyFlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': (
            'url',
            'title',
            'content',
            'sites'
        )}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)
admin.site.register(HomePage)
