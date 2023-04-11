from django.contrib.auth.models import User
from django.db import models
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
    date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=150)
    main_page_img = models.ImageField(upload_to='home/post_images/main_page_images',
                                      null=True, blank=True)

    post_cover_img = models.ImageField(upload_to='home/post_images/post_covers',
                                       null=True, blank=True)

    post_size = models.IntegerField(default=0)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    travelers = models.ManyToManyField(Traveler)
    postLatitude = models.FloatField(null=True, blank=True)
    postLongitude = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        return super().save(*args, **kwargs)


class PostArticle(models.Model):
    title = models.CharField(max_length=70)
    text_block = models.TextField()
    image = models.ImageField(upload_to='home/article_images/', null=True, blank=True)
    post_name = models.ForeignKey(Post,
                                  on_delete=models.SET_NULL,
                                  null=True, blank=True,
                                  related_name='articles')

    def __str__(self):
        return f'{str(self.title)} | {str(self.post_name)}'


class PostPoint(models.Model):
    name = models.CharField(max_length=70)
    longitude = models.FloatField()
    latitude = models.FloatField()
    image = models.ImageField(upload_to='home/point_images/', null=True, blank=True)
    post_name = models.ForeignKey(Post,
                                  on_delete=models.SET_NULL,
                                  null=True, blank=True,
                                  related_name='points')

    def __str__(self):
        return f'{str(self.name)} | {str(self.post_name)}'
