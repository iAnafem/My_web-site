from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Model representing a posts' category"""
    name = models.CharField(max_length=20)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Post(models.Model):
    """Model representing a post"""
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    cover = models.FileField(upload_to='images/blog/', null=True, blank=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        return reverse('post_detail', args=[str(self.pk)])


class Comment(models.Model):
    """Model representing a projects' commentary"""
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
