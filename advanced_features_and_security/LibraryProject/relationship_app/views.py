from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import permission_required

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"books: books"}
    return render (request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["books"] = self.objects.book.all()
        return context


# Login View (built-in)
class UserLoginView(LoginView):
    template_name = "relationship_app/login.html"


# Logout View (built-in)
class UserLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


# Registration View (custom, uses built-in form)
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("book_list_function")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, "relationship_app/register.html", context)

@permission_required("relationship_app.can_view_book", raise_exception=True)
def book_list_view(request):
    ...