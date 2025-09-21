from django import forms
from . import models

class ArticlePost(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ['title', 'text']