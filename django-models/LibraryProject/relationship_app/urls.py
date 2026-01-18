from django.urls import path
from .views import book_list, LibraryDetailView

urlpatterns = [
    path("books/", book_list, name="books"),
    path("libraries/", LibraryDetailView.as_view, name="libraries")
]