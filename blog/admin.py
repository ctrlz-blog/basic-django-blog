from django.contrib import admin

from blog import models

from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
    list_display = ["title", "status"]


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag, admin.ModelAdmin)
admin.site.register(models.Category, admin.ModelAdmin)
