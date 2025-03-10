from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book,Author, Librarian
from .models import Library

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    book_list = [f"{book.title} by {book.author.name}" for book in books]
    return render(request, "relationship_app/list_books.html", {"book_list": book_list})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books_in_library"] = self.object.books.all()
        return context
