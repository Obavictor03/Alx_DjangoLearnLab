from django.urls import path
from .views import book_list, BookDetailView

urlpatterns = [
    path("books/", book_list, name="books"),
    path("books/", BookDetailView.as_view, name="books")
]