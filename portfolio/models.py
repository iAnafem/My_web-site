from django.db import models
from django.urls import reverse


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
    main_image = models.FileField(upload_to='images/portfolio/', null=True, blank=True)
    full_description = models.TextField(max_length=2500, null=True, blank=True)
    full_description_2 = models.TextField(blank=True, default='')

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title


class ProjectComment(models.Model):
    """Model representing post comments"""
    author = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.SET_NULL,
        null=True, related_name='project_author',
    )
    body = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project_comments')

    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        if self.project.category.name.startswith('Soft'):
            return reverse('software_project_detail', args=[self.project_id])
        else:
            return reverse('civil_project_detail', args=[self.project_id])


class ProjectImages(models.Model):
    """Model representing images for project full description"""
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True, related_name='content_images')
    image = models.FileField(upload_to='images/portfolio/', null=True, blank=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.project) + ".content_image." + str(self.id)


