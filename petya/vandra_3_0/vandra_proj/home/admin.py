from django.contrib import admin
# from django.contrib.gis.admin import GISModelAdmin

from home.models import Post, Traveler, PostArticle

admin.site.register(Post)

admin.site.register(Traveler)

admin.site.register(PostArticle)



# @admin.register(Post)
# class PostAdmin(GISModelAdmin):
#     default_lon = 27
#     default_lat = 53
#     # default_zoom
#     list_display = ('id', 'title')

