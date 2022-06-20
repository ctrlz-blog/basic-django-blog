from django.contrib import admin

from blog import models

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]


admin.site.register(models.Post, PostAdmin)
