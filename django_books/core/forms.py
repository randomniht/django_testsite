from django import forms
from .models import Category, Book


class AddBookForm(forms.Form):
    name = forms.CharField(label='Book name')
    author = forms.CharField(label='Author')
    price = forms.CharField(label= 'price')
    category = forms.ModelChoiceField(queryset=Category.objects.all())


    def clean(self):
        name = self.cleaned_data['name']
        if Book.objects.filter(name = name).exists():
            raise forms.ValidationError('this book exist')

class AddCategoryForm(forms.Form):
    name = forms.CharField(label='Category name')


    def clean(self):
        name = self.cleaned_data['name']
        if Category.objects.filter(name = name).exists():
            raise forms.ValidationError('this category exist')
