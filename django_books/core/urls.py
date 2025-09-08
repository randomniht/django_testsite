from django.urls import path

from .views import *


urlpatterns = [
    path('', hello),
    path('books', books),
    path('books/add', add_book),
    path('categories/add', add_category),
    path('contacts', contacts),
    path('reviews',reviews),
    path('reviews/add',add_review)
    ]