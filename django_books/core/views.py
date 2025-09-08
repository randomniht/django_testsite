from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Book, Category, Contact, BookReview

def hello(request):
    """Главная страница"""

    return render(request, 'main.html')


def books(request):
    """Страница со списком книг"""

    books_list = Book.objects.all()
    category_list = Category.objects.all()

    category_id_from_url = request.GET.get('category')
    if category_id_from_url:
        print(category_id_from_url)
        books_list = books_list.filter(category__id=category_id_from_url)

    context = {'books_list': books_list, 'category_list':category_list }

    return render(request, 'books.html', context)


def add_book(request):
    """Добавление книги"""
    # обрабатываем POST запрос
    category_list = Category.objects.all()
    errors = ''

    if request.method == 'POST':
        # вернет либо None либо данные
        name_from_form = request.POST.get('name')
        author_from_form = request.POST.get('author')
        price_from_form = request.POST.get('price')
        category_from_form = request.POST.get('category')

        if name_from_form and author_from_form:
            # достаем объект с категории
            if category_from_form:
                category = Category.objects.get(id=category_from_form)
            else:
                category = None

            book = Book(name=name_from_form,
                        author=author_from_form,
                        price=price_from_form, category=category)
            book.save()
            return redirect('/books')
        else:
            errors = 'Не заполнено название либо автор'

    context = {'category_list': category_list, 'errors': errors}

    return render(request, 'add_book.html', context)

def add_category(request):
    errors =''
    success_message = ''
    print(request.POST)
    if request.method == 'POST':
        category_name = request.POST.get('name')
        if category_name:
            Category.objects.create(name = category_name)
            success_message = 'category add'
        else:
            errors = 'Заполните поля'
    context ={'errors': errors, 'success_message' : success_message}
    return render(request,'add_category.html', context)

def contacts(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    
    return render(request, 'contacts.html', context)

def reviews(request):
    reviews = BookReview.objects.all()
    context = {'reviews': reviews}
    return render(request, 'reviews.html', context)

def add_review(request):
    print(request.POST)
    books = Book.objects.all()
    if request.method == 'POST':
        text = request.POST.get('text')
        book_id = request.POST.get('book')
        if text and book_id:
            book = Book.objects.get(id = book_id)
            BookReview.objects.create(text = text, book = book)
            return redirect('/reviews')
    context = {'books': books}
    return render(request, 'add_review.html', context)