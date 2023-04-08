from django.contrib.auth.models import User
# from django.db import models
from django.contrib.gis.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Traveler(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to='home/travelers_avatars',
                               null=True, blank=True)

    def __str__(self):
        return self.first_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    main_page_img = models.ImageField(upload_to='home/post_images/main_page_images',
                                      null=True, blank=True)

    post_size = models.IntegerField(default=0)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    travelers = models.ForeignKey(Traveler,
                                  on_delete=models.SET_NULL, null=True, blank=True)
    location = models.PointField(srid=4326, null=True, blank=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        return super().save(*args, **kwargs)
