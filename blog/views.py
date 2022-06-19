from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Post
# Create your views here.

def index(request: HttpRequest) -> HttpResponse:

    published_posts = Post.objects.filter(status="published")

    context = {
        "posts": published_posts
    }

    return render(request, "index.html", context)