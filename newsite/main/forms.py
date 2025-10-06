from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
                                                  
class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1', 'password2')


class ArticlePost(forms.ModelForm):
    class Meta:
        model = models.Articles
        fields = ['title', 'text','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']

    
class PostMedia(forms.ModelForm):
    class Meta:
        model = models.Mediapost
        fields = ['image']
