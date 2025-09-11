from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Book, Category, Contact, BookReview
from .forms import AddBookForm, AddCategoryForm

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



def add_book_form(request):

    book_form = AddBookForm()
    if request.method == 'POST':
        book_form = AddBookForm(request.POST)
        if book_form.is_valid():
            name = book_form.cleaned_data['name']
            author = book_form.cleaned_data['author']
            price = book_form.cleaned_data['price']
            category = book_form.cleaned_data['category']

            Book.objects.create(name=name, author = author, price = price, category = category)
            return redirect('/books')

    print(request.POST)
    context = {'book_form':book_form}

    return render(request, 'add_book_form.html', context)


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

def add_category_form(request):
    category_form = AddCategoryForm()
    if request.method == 'POST':
        category_form = AddCategoryForm(request.POST)
        if category_form.is_valid():
            name = category_form.cleaned_data['name']
            Category.objects.create(name = name)
            return redirect('/books')
    context = {'category_form': category_form}
    return render(request, 'add_category_form.html', context )

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
            return redirect('/  reviews')
    context = {'books': books}
    return render(request, 'add_review.html', context)

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book':book}
    return render(request, 'book_detail.html', context)