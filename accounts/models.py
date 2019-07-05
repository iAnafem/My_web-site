from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=30, null=True, blank=True)
    avatar = models.FileField(upload_to='images/accounts/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    biography = models.TextField(max_length=1000, null=True, blank=True)
    comments = models.ForeignKey('blog.comment', on_delete=models.CASCADE, null=True,)
