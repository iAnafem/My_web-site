from django.db import models


class Home(models.Model):
    """Model representing a project's category"""
    name = models.CharField(max_length=200, help_text="Enter a project's category")
    projects = models.ForeignKey('portfolio.Project',  on_delete=models.SET_NULL, null=True)
    categories = models.ForeignKey('portfolio.Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object (in admin site etc.)"""
        return self.name
