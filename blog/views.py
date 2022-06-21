from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Post
from blog.forms import AddPostForm
# Create your views here.


def index(request: HttpRequest) -> HttpResponse:

    published_posts = Post.objects.filter(status="published")

    context = {
        "posts": published_posts
    }

    return render(request, "index.html", context)


def add_post(request):

    form = AddPostForm()

    context = {
        "form": form
    }

    return render(request, "add_post.html", context)
