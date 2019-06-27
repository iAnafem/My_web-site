from django.db import models


class Blog(models.Model):
    """Model representing a project's category"""
    name = models.CharField(max_length=200, help_text="Enter a project's category")

    def __str__(self):
        """String for representing the Model object (in admin site etc.)"""
        return self.name
