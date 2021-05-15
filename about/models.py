from django.db import models

# About Model

'''
This class will capture all straight forwad about attributes of the
about model. Name, Profile Picture, Descrption, Current Position,

It will contain helper classes which handle one to many relations
'''


class About(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    profile_pic = models.ImageField(upload_to='profiles')
    brief_desc = models.TextField(blank=False, help_text='About You')
    position = models.TextField(blank=False, help_text='current Position')

    def __str__(self):
        return self.name
