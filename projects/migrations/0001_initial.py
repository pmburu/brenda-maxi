# Generated by Django 3.2.2 on 2021-05-12 23:38

from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('project_feature_image', models.ImageField(upload_to='images/projects/feature_image')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_detail_description', models.CharField(max_length=200)),
                ('home_hero_image', models.ImageField(upload_to='images/projects/hero')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_details', to='projects.project')),
            ],
            options={
                'verbose_name': 'project_detail',
                'verbose_name_plural': 'project_details',
                'db_table': 'project_detail',
            },
        ),
        migrations.CreateModel(
            name='ProjectGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=projects.models.upload_project_detail_images)),
                ('project_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_galleries', to='projects.projectdetail')),
            ],
        ),
    ]
