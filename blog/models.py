from django.db import models
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    """Model representing a posts' category"""
    name = models.CharField(max_length=20)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Post(models.Model):
    """Model representing a post"""
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    cover = models.FileField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular post instance."""
        return reverse('post_detail', args=[str(self.pk)])


class Comment(models.Model):
    """Model representing post comments"""
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.SET_NULL, null=True, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
