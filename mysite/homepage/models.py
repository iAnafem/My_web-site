from django.db import models


class HomePage(models.Model):
    """Model representing the content on the home page from the other applications"""
    name = models.CharField(max_length=200, help_text="Name")
    projects = models.ManyToManyField('portfolio.Project', related_name='projects')
    posts = models.ManyToManyField('blog.Post', related_name='posts')

    def __str__(self):
        """String for representing the Model object (in admin site etc.)"""
        return self.name

