from django.urls import path
from .import views


urlpatterns = [
    path('', views.BooksListView.as_view(), name='main'),
    path('detail_book/<slug:slug>/', views.BooksDetailView.as_view(), name='detail_book'),
    path('category_book/<slug:cat_slug>/', views.CategoryView.as_view(), name='category'),
]
