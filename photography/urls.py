from django.urls import path

from . import views

urlpatterns = [
    path('photography/', views.photography, name='photography')
]
