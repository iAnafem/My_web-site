# Generated by Django 2.2.2 on 2019-06-27 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20190627_1012'),
        ('homepage', '0003_auto_20190627_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='categories',
        ),
        migrations.AddField(
            model_name='home',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.Category'),
        ),
        migrations.RemoveField(
            model_name='home',
            name='projects',
        ),
        migrations.AddField(
            model_name='home',
            name='projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.Project'),
        ),
    ]