from django.shortcuts import render

from .models import Photography

# Photography views


def photography(request):

    template_name = 'image-gallery.html'
    photos = Photography.objects.all()

    return render(
        request,
        template_name,
        {
            'photos': photos
        }
    )
