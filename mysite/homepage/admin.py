from django.contrib import admin
from django.db import models
from .models import HomePage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _


# Define a new FlatPageAdmin


class MyFlatPage(FlatPage):
    header1 = models.CharField(_('header1'), max_length=200, blank=True, null=True)
    header2 = models.CharField(_('header2'), max_length=200, blank=True, null=True)
    text_field = models.CharField(_('text_field'), max_length=200, blank=True, null=True)
    content1 = models.TextField(_('content1'), blank=True, null=True)
    content2 = models.TextField(_('content2'), blank=True, null=True)
    content3 = models.TextField(_('content3'), blank=True, null=True)

# Re-register FlatPageAdmin


class MyFlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': (
            'url',
            'title',
            'header1',
            'header2',
            'text_field',
            'content',
            'content1',
            'content2',
            'content3',
            'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )

    list_display = ('url', 'title')
    list_filter = ('sites', 'registration_required')
    search_fields = ('url', 'title')


admin.site.unregister(FlatPage)
admin.site.register(MyFlatPage, MyFlatPageAdmin)
admin.site.register(HomePage)
