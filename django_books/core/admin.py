from django.contrib import admin

from .models import Book, Category, Contact, BookReview

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Contact)

@admin.register(BookReview)
class BookReviewAdmin(admin.ModelAdmin):
    list_display = ["text", "book"]
