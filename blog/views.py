from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post
from blog.forms import PostForm


def index(request: HttpRequest) -> HttpResponse:

    published_posts = Post.objects.filter(status="published").order_by("published_date")

    context = {"posts": published_posts}

    return render(request, "index.html", context)


def add_post(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            # form.save() creates a post from the form
            post = form.save()

            return redirect("post_detail", slug=post.slug)

    else:
        form = PostForm()

    context = {"form": form, "edit_mode": False}

    return render(request, "post_form.html", context)


def post_detail(request: HttpRequest, slug: str) -> HttpResponse:

    post = get_object_or_404(Post, slug=slug)

    context = {"post": post}
    return render(request, "post_detail.html", context)


def publish(request: HttpRequest, slug: str) -> HttpResponse:

    post = get_object_or_404(Post, slug=slug)
    post.publish()

    return redirect("index")


def edit_post(request: HttpRequest, slug: str) -> HttpResponse:

    post = get_object_or_404(Post, slug=slug)

    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", slug=post.slug)

    context = {"form": form, "post": post, "edit_mode": True}
    return render(request, "post_form.html", context)


def delete_post(request: HttpRequest, slug: str) -> HttpResponse:

    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect("index")

    context = {"post": post}

    return render(request, "delete_post.html", context)
