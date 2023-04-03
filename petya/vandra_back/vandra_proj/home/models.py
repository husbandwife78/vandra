from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    post_size = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)



