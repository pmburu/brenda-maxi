from django.db import models

# External Library
from embed_video.fields import EmbedVideoField

# Cinematography Model


class Cinematography(models.Model):
    video = EmbedVideoField(
        verbose_name="My video", help_text="Copy & Paste YouTube link here"
    )
    video_caption = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.video_caption

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
