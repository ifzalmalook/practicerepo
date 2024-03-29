# Generated by Django 4.2.11 on 2024-03-18 20:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_category_alter_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='project_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
