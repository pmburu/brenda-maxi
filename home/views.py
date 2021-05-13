from django.shortcuts import render

from projects.models import ProjectDetail

# Home Page View

'''
A class to fetch from Project Detail models and render
the hero image, project name and project description
'''


def home(request):
    template_name = 'index.html'

    home_details = ProjectDetail.objects.all()[:3]
    return render(
        request,
        template_name,
        {
            'home_details': home_details
        }
    )
