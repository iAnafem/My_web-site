from django.contrib import admin
from .models import Category, Project, ProjectComment, ProjectImages


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'category',
                    'short_description',
                    'technologies',
                    'full_description',
                    'main_image',
                    )
    fields = ['title',
              'category',
              'short_description',
              'technologies',
              'full_description',
              'main_image',
              ]


admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectComment)
admin.site.register(ProjectImages)