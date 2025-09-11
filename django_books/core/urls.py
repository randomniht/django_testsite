from django.urls import path

from .views import *


urlpatterns = [
    path('', hello),
    path('books', books),
    path('books/add', add_book_form),
    path('books/<int:book_id>', book_detail),
    path('categories/add', add_category_form),
    path('contacts', contacts),
    path('reviews',reviews),
    path('reviews/add',add_review)
    ]

