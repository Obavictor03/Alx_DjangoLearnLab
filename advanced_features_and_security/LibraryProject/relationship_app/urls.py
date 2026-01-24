from django.urls import path
from .views import list_books, LibraryDetailView, UserLoginView, UserLogoutView, register_view
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app import views


urlpatterns = [
    path("books/", list_books, name="books"),
    path("libraries/", LibraryDetailView.as_view, name="libraries"),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path(
        "register/",
        views.register,
        name="register",
    ),
]