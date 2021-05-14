from django.urls import path

from . import views

urlpatterns = [
    path('videos', views.cinema_gallery, name='videography')
]
