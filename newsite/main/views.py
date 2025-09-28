from django.shortcuts import render, redirect
from .models import Articles
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    logout(request)  # только выполняет выход
    messages.success(request, 'Вы вышли из системы')
    return redirect('/')  # обязательно возвращаем redirect




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