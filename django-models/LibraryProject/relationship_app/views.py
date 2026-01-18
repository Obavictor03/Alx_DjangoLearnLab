from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {"books: books"}
    return render (request, 'relationship_app/list_books.html', context)

class BookDetailView(DetailView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'books'