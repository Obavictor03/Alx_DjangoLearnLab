import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """Query all books by a specific author"""
    books = Book.objects.filter(author__name=author_name)

    print(f"\nBooks written by {author_name}:")
    for book in books:
        print(f"- {book.title}")


def list_books_in_library(library_name):
    """List all books in a library"""
    books = Book.objects.filter(library__name=library_name)

    print(f"\nBooks available in {library_name} library:")
    for book in books:
        print(f"- {book.title} by {book.author.name}")


def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        print(f"\nLibrarian for {library_name} library:")
        print(f"- {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"\nNo librarian assigned to {library_name} library.")


# Sample execution
if __name__ == "__main__":
    query_books_by_author("Chinua Achebe")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
