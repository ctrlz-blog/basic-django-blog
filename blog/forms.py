from django import forms
from . import models

from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "body", "category", "tags", "feature_image"]

    body = forms.CharField(widget=SummernoteWidget)

    tags = forms.ModelMultipleChoiceField(
        queryset=models.Tag.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    category = forms.ModelChoiceField(
        queryset=models.Category.objects.all(), widget=forms.RadioSelect
    )
