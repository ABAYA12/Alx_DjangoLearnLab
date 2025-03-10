from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import register_view, login_view, logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", list_books, name="list_books"),
    path("library/<int:pk>", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
