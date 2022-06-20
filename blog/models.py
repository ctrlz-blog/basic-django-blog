from django.db import models

from autoslug import AutoSlugField

# Create your models here.


class Post(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="title")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="draft"
    )

    body = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    @property
    def excerpt(self):
        character_limit = 150
        if len(self.body) < character_limit:
            excerpt = self.body
        else:
            excerpt = self.body[:character_limit]+"..."

        return excerpt

    def __str__(self):
        return self.title
