from django.shortcuts import render, redirect
from .models import Articles
from . import forms
# Create your views here.

def main(request):
    elements = Articles.objects.all()
    context ={'elements':elements}
    return render(request,'main.html', context)

def posting(request):
    if request.method == 'POST':
        form = forms.ArticlePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.save()
            return redirect('/')
    else:
        form = forms.ArticlePost()
    context = {'form':form}
    return render(request, 'posts.html', context)

