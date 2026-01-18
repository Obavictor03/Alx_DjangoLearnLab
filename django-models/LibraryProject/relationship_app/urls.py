from django.urls import path
from .views import list_books, LibraryDetailView, UserLoginView, UserLogoutView, register_view


urlpatterns = [
    path("books/", list_books, name="books"),
    path("libraries/", LibraryDetailView.as_view, name="libraries"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("register/", register_view, name="register"),
]