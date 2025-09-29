from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, Comment
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.





def main(request):
    elements = Articles.objects.all()
    context ={'elements':elements}
    return render(request,'main.html', context)


@login_required(login_url='/log/')
def posting(request):
    if request.method == 'POST':
        form = forms.ArticlePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user  # привязываем к пользователю
            newpost.save()
            return redirect('/')
    else:
        form = forms.ArticlePost()
    context = {'form': form}
    return render(request, 'posts.html', context)


def registr(request):
    if request.method == 'POST':
        user_form = forms.RegForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)  # ← автоматический вход после регистрации
            return redirect('/')
    else:
        user_form = forms.RegForm()
    context = {'user_form': user_form}
    return render(request, 'registration_form.html', context)



def user_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')
                return redirect('/')
            else:
                messages.error(request, 'Неверные данные')
    else:
        form = forms.LoginForm()
    
    context = {'form': form}
    return render(request, 'login.html', context)

from django.contrib.auth import logout

def user_logout(request):
    logout(request)  #выполняет выход
    messages.success(request, 'Вы вышли из системы')
    return redirect('/')

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Articles, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    
    if request.method == 'POST':
        # Отправка нового комментария
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = forms.CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'post_detail.html', context)





@login_required
def delete_article(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if article.author != request.user:
        html_content = """
            <h1>403 Forbidden</h1>
            <p>U cant del foreign post</p>
            <a href="/" class="btn btn-info rounded-pill px-3">Main page</a>
        """
        return HttpResponse(html_content, content_type='text/html', status=403)




# def registr(request):
#     if request.method == 'POST':
#         user_form = forms.RegForm(request.POST)
#         if user_form.is_valid():

#             user_form.save()
#             return redirect('/')
#     else:
#         user_form = forms.RegForm()
#     context = {'user_form':user_form}
#     return render(request, 'registration_form.html', context)


# def posting(request):
#     if request.method == 'POST':
#         form = forms.ArticlePost(request.POST, request.FILES)
#         if form.is_valid():
#             newpost = form.save(commit=False)
#             newpost.save()
#             return redirect('/')
#     else:
#         form = forms.ArticlePost()
#     context = {'form':form}
#     return render(request, 'posts.html', context)