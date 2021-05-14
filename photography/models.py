from django.db import models

# Photography Models


class Photography(models.Model):
    photo = models.ImageField(upload_to='images/photography')
    photo_caption = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.photo_caption

    class Meta:
        verbose_name = 'Photograph'
        verbose_name_plural = 'Photographs'
