# Generated by Django 2.2.3 on 2019-07-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_auto_20190712_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimages',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
