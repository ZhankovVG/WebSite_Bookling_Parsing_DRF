from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import *
from django.db.models import Q
from .forms import *
from cart.forms import CartAddBookForm

from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializer import *
from .servise import PageNumberPagination


class Mixin():
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs) 
        context["categories"] = Category.objects.all()
        context['star_form'] = RatingForm()
        context['cart_book_form'] = CartAddBookForm()
        return context
    

class BooksListView(Mixin, ListView):
    # Output Books
    model = Books
    queryset = Books.objects.filter(draft=False)
    paginate_by = 4


class BooksDetailView(Mixin, DetailView):
    # Full books description
    model = Books
    slug_field = 'url'


class CategoryView(Mixin, ListView):
    # Book listing by category
    model = Books
    template_name = 'bookstore_app/books_list.html'

    def get_queryset(self):
        category = get_object_or_404(Category, url=self.kwargs['cat_slug'])
        return Books.objects.filter(category=category)
    

class SearchView(Mixin, ListView):
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
    

class AddStarsRating(View):
    # Adding book ratings
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Reting.objects.update_or_create(
                ip=self.get_client_ip(request),
                book_id=int(request.POST.get("book")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
        
        
class MixinApi():
    # class mixin
    serializers_class = None
    queryset = Books.objects.filter(draft=False)
    pagination_class = PageNumberPagination
    permission_classes = [permissions.IsAuthenticated]

               
class BookApiView(MixinApi, generics.ListAPIView):
    # Book list output
    serializer_class = BookListSerializer
    
    
class BookDetailApiView(MixinApi, generics.RetrieveAPIView):
    # full description book    
    serializer_class = BookDetailSerilizer
    
    
class CommentApiView(MixinApi, generics.CreateAPIView):
    # Output comments
    serializer_class = CommetCreateSerializer