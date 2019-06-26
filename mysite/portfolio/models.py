from django.db import models


class Category(models.Model):
    """Model representing a project's category"""
    name = models.CharField(max_length=200, help_text="Enter a project's category")

    def __str__(self):
        """String for representing the Model object (in admin site etc.)"""
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    short_description = models.TextField()
    technology = models.CharField(max_length=500)
    main_image = models.FilePathField(path="img/", null=True)
    full_description = models.TextField()
    full_description_images = models.FilePathField(path="img/", null=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title


class Comment(models.Model):
    """Model representing comments to projects"""
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Project', on_delete=models.CASCADE)

