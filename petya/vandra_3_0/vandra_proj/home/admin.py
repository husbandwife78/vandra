from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from home.models import Post, Traveler

admin.site.register(Traveler)

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(GISModelAdmin):
    default_lon = 27
    default_lat = 53
    # default_zoom
    list_display = ('id', 'title')
# class MemberAdmin(admin.ModelAdmin):
#     list_display = ("title", "updated",)
#     prepopulated_fields = {"slug": "title"}
