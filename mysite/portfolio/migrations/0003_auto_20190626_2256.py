# Generated by Django 2.2.2 on 2019-06-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190626_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='full_description_images',
            field=models.FileField(null=True, upload_to='static/img/'),
        ),
    ]
