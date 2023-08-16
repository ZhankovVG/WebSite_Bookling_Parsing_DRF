from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import *
from django.db.models import Q
from .forms import CommentsForm


class CategoryOutputView():
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["categories"] = Category.objects.all()
        return context
    

class BooksListView(CategoryOutputView, ListView):
    # Output Books
    model = Books
    queryset = Books.objects.filter(draft=False)
    paginate_by = 4


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
    

class SearchView(CategoryOutputView, ListView):
    # Search books
    def get_queryset(self):
        query = self.request.GET.get('search')
        return Books.objects.filter(
            Q(name__icontains=query) | Q(code__contains=query)
            )
    

class CommentsView(View):
    # Comments
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        book = Books.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.save()
        return redirect(book.get_absolute_url())