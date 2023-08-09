from django.urls import path
from .import views


urlpatterns = [
    path('', views.BooksListView.as_view(), name='main'),
]
