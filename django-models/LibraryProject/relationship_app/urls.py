from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="books"),
    path("libraries/", LibraryDetailView.as_view, name="libraries")
]