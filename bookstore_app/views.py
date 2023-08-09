from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class BooksListView(ListView):
    model = Books
    queryset = Books.objects.filter(draft=False)