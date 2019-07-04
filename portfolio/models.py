from django.db import models


class Category(models.Model):
    """Model representing a projects' category"""
    name = models.CharField(max_length=200, help_text="Enter a project's category")

    def __str__(self):
        """String for representing the Model object (in admin site etc.)"""
        return self.name


class Project(models.Model):
    """Model representing a project"""
    title = models.CharField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    short_description = models.TextField()
    technologies = models.CharField(max_length=500)
    main_image = models.FilePathField(path="img/", null=True, blank=True)
    full_description = models.TextField()

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title


class Comment(models.Model):
    """Model representing comments to projects"""
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Project', on_delete=models.CASCADE)


def set_main_img(query, name):
    """This method sets the main images to projects"""
    for i, project in enumerate(query.filter(category__name__contains=name)):
        p = project
        p.main_image = f'portfolio/img/{name}_project{str(i)}.jpg'
        p.save()



