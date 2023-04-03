from django.contrib import admin

from home.models import Post, Traveler

admin.site.register(Post)
admin.site.register(Traveler)



# class MemberAdmin(admin.ModelAdmin):
#     list_display = ("title", "updated",)
#     prepopulated_fields = {"slug": "title"}
