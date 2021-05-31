from django.db import models

# Models in the Project module

'''
This is a class that creates the project table in the database and
populates it with an automatic id (int). Additionally, it will populate
the table with a project name and project feature image.
'''


class Project(models.Model):
    project_name = models.CharField(max_length=200, blank=False, null=False)
    project_feature_image = models.FileField(
        upload_to='images/projects/feature_image'
    )

    def __str__(self):
        return self.project_name

    class Meta:
        db_table = 'project'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


'''
This is a class that creates the project_details table in the database and
populates it with an automatic id (int), it will also have a one to one
relationship with the project table in that, there is only one project with
one project detail (depicted with a foreign key at the database level).
Other attributes in the table include: homepage hero image and
project_detail_description
'''


class ProjectDetail(models.Model):
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name='project_details'
    )
    project_detail_description = models.TextField(
        null=False, blank=False
    )
    home_hero_image = models.FileField(
        upload_to='images/projects/hero'
    )

    def __str__(self):
        return self.project.project_name

    class Meta:
        db_table = 'project_detail'
        verbose_name = 'Project Detail'
        verbose_name_plural = 'Project Details'


'''
This is a helper function to save the uploaded project detail images
into a structured directory. The directory looks like this:
images/projects/name_of_project/filename
'''


def upload_project_detail_images(instance, filename):
    return 'images/projects/{}/{}'.format(
        instance.project_detail.project.project_name,
        filename
    )


'''
This class creates a one to many relationship with the project detail table.
It becomes a nested data. In that one project has one or many images.
'''


class ProjectGallery(models.Model):
    image = models.FileField(upload_to=upload_project_detail_images)
    project_detail = models.ForeignKey(
        ProjectDetail,
        on_delete=models.CASCADE,
        related_name='project_galleries'
    )
