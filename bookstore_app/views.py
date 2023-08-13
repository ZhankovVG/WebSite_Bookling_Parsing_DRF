from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import *


class CategoryOutputView():
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["categories"] = Category.objects.all()
        return context
    

class BooksListView(CategoryOutputView, ListView):
    # Output Books
    model = Books
    queryset = Books.objects.filter(draft=False)


class BooksDetailView(CategoryOutputView, DetailView):
    # Full books description
    model = Books
    slug_field = 'url'


class CategoryView(CategoryOutputView, ListView):
    # Book listing by category
    model = Books
    template_name = 'bookstore_app/books_list.html'

    def get_queryset(self):
        category = get_object_or_404(Category, url=self.kwargs['cat_slug'])
        return Books.objects.filter(category=category)