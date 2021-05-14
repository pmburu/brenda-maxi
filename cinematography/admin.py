from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import Cinematography

# Cinemagraphs Admin interface


class CinemaAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Cinematography, CinemaAdmin)
