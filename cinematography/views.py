from django.shortcuts import render

from .models import Cinematography


# Cinematography Views.

def cinema_gallery(request):

    template_name = 'video-gallery.html'
    videos = Cinematography.objects.all()

    return render(
        request,
        template_name,
        {
            'videos': videos
        }
    )
