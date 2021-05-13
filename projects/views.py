from django.shortcuts import render

from .models import (
    Project,
    ProjectDetail
)

# Projects Views

'''
A function to query all project objects and render
them through the projects.html file.
'''


def projects(request):
    template_name = 'projects.html'
    featured_projects = Project.objects.all()

    return render(
        request,
        template_name,
        {
            'featured_projects': featured_projects
        }
    )


'''
A function to query all project details based on specific
primary keys and render the project-details.html file.
'''


def project_details(request, project_id):
    template_name = 'project-details.html'
    details = ProjectDetail.objects.get(pk=project_id)

    return render(
        request,
        template_name,
        {
            'details': details
        }
    )
