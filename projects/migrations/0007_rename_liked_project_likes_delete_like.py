# Generated by Django 4.2.11 on 2024-03-20 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_liked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='liked',
            new_name='likes',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
