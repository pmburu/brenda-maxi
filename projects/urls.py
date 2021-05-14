from django.urls import path

from . import views

urlpatterns = [
    path('project/', views.projects, name='projects'),
    path('project/<int:project_id>/',
         views.project_details, name='project-details')
]
