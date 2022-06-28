from django import forms
from . import models


# forms.py

from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "body", "category", "tags"]

    tags = forms.ModelMultipleChoiceField(
        queryset=models.Tag.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    category = forms.ModelChoiceField(
        queryset=models.Category.objects.all(), widget=forms.RadioSelect
    )
