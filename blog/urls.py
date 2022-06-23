from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_post, name="add_post"),
    path("<slug:slug>", views.post_detail, name="post_detail"),
    path("<slug:slug>/publish", views.publish, name="publish"),
    path("<slug:slug>/edit", views.edit_post, name="edit"),
    path("<slug:slug>/delete", views.delete_post, name="delete"),
]
