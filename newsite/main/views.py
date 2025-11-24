from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, Comment, Mediapost, Word, Note
from . import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
# Create your views here.


@require_POST
@login_required(login_url='/log/')
def like_article(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    
    if article.liked_by.filter(id=request.user.id).exists():
        # Убираем лайк
        article.liked_by.remove(request.user)
        is_liked = False
    else:
        # Добавляем лайк
        article.liked_by.add(request.user)
        is_liked = True
    
    return JsonResponse({
        'likes': article.likes_count,
        'is_liked': is_liked
    })


def main(request):
    elements = Articles.objects.all().order_by('-date')
    
    # Подготавливаем данные о лайках
    articles_data = []
    for article in elements:
        articles_data.append({
            'article': article,
            'user_has_liked': article.user_has_liked(request.user)
        })
    
    context = {
        'articles_data': articles_data,
        'current_user': request.user
    }
    return render(request, 'main.html', context)


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
            login(request, user)  #  автоматический вход после регистрации
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
                messages.success(request, f'Welcome, {username}!')
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
    messages.success(request, 'U logout')
    return redirect('/')

@login_required(login_url='/log/')
def post_detail(request, pk):
    
    post = get_object_or_404(Articles, pk=pk)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    
    if request.method == 'POST':
        # отправка нового комментария
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





# @login_required(login_url='/log/')
def delete_article(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    if article.author != request.user:
        html_content = """
            <h1>403 Forbidden</h1>
            <p>U cant del foreign post</p>
            <a href="/" class="btn btn-info rounded-pill px-3">Main page</a>
        """
        return HttpResponse(html_content, content_type='text/html', status=403)
    article.delete()
    return redirect('/')


def draw_page(request):
    test = 1
    context = {'test': test}
    return render(request, 'draw_page.html', context=context)


@login_required(login_url='/log/')
def randmed(request):
    elements = Mediapost.objects.filter(image__isnull=False).exclude(image__exact='')
    # инициализация формы

    if request.method == 'POST':
        form = forms.PostMedia(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('/randphoto')
    else:
        form = forms.PostMedia()

    context = {'elements': elements, 'form': form}
    return render(request, 'randmed.html', context=context)
    


def snake_game(request):
    return render(request, 'snake.html')


@login_required(login_url='/log/')
def words(request):
    status = request.GET.get('status')

    if status == 'learned':
        all_words = Word.objects.filter(is_done=True)
    else:
        all_words = Word.objects.all()
    
    if request.method == 'POST':
        text = request.POST.get('text').strip()
        translate = request.POST.get('translate').strip()

        if Word.objects.filter(text__iexact=text).exists():
            messages.error(request, 'word_exist')
        else:
            Word.objects.create(text=text, translate=translate, created_by=request.user)

        return redirect('words')
    
    return render(request, 'word_main.html', {'words': all_words, 'status': status})

@login_required(login_url='/log/')
def words_detail(request, word_id):
    word = get_object_or_404(Word, pk=word_id)

    if request.method == 'POST' and 'note' in request.POST:
        note_text = request.POST.get('note')
        if note_text:
            Note.objects.create(word=word, text=note_text, created_at=timezone.now())
        return redirect('words_detail', word_id=word_id)

    if request.method == 'POST' and 'mark_done' in request.POST:
        word.is_done = True
        word.save()
        return redirect('words_detail', word_id=word_id)

    notes = word.notes.all()

    context = {
        'word': word,
        'notes': notes,
    }
    return render(request, 'word_detail.html', context)


@login_required(login_url='/log/')
def word_delete(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    if request.method == 'POST':
        word.delete()
        return redirect('words')
    return render(request, {'word': word})















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