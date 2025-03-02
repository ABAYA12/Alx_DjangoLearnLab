from django.urls import path
from relationship_app.views import LibraryDetailView, list_books

urlpatterns = [
    path("", list_books, name="list_books"),
    path("library/<int:pk>", LibraryDetailView.as_view(), name="library_detail"),
]