from django.urls import path
from .import views


urlpatterns = [
    path('', views.BooksListView.as_view(), name='main'),
    path('detail_book/<slug:slug>/', views.BooksDetailView.as_view(), name='detail_book'),
    path('category_book/<slug:cat_slug>/', views.CategoryView.as_view(), name='category'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('comments/<int:pk>/', views.CommentsView.as_view(), name='comments'),
    path('add-rating/', views.AddStarsRating.as_view(), name='add-rating'),
    # added URLs for DRF api
    path('api/v1/book/', views.BookApiView.as_view()),
    path('api/v1/book/<int:pk>/', views.BookDetailApiView.as_view()),
    path('api/v1/book/review/', views.CommentApiView.as_view()),
]
