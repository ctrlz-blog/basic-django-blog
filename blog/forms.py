from django import forms
from . import models


class AddPostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body']
