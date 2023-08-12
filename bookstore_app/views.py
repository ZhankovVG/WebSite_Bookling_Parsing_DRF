from django.shortcuts import render
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