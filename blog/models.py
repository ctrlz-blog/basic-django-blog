from datetime import datetime

from django.db import models

from autoslug import AutoSlugField

class Tag(models.Model):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="title", unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")

    body = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    tags = models.ManyToManyField(to=Tag, related_name="posts", blank=True)

    @property
    def excerpt(self):
        character_limit = 150
        if len(self.body) < character_limit:
            excerpt = self.body
        else:
            excerpt = self.body[:character_limit] + "..."

        return excerpt

    def save(self):
        self.updated_date = datetime.now()
        super().save()

    def publish(self):
        self.published_date = datetime.now()
        self.status = "published"
        self.save()

    def __str__(self):
        return self.title

