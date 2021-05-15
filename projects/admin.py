from django.contrib import admin
from .models import (
    Project,
    ProjectDetail,
    ProjectGallery
)

# Model Registration

'''
register(*models, site=django.contrib.admin.sites.site) is used for
registraton of models into the admin interface
'''

admin.site.register(Project)


'''
subclass that uses the TabularInline class in django admin to manipulate
the ProjectGallery forms in order to be presented in a tabular style.
'''


class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery


'''
decorator used to register ProjectDetail model into the
ModelAdmin class
'''


@admin.register(ProjectDetail)
class ProjectDetailAdmin(admin.ModelAdmin):
    inlines = [
        ProjectGalleryInline
    ]
