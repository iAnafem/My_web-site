# Generated by Django 2.2.3 on 2019-07-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_remove_project_full_description_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='main_image',
            field=models.FilePathField(blank=True, null=True, path='portfolio/img/'),
        ),
    ]