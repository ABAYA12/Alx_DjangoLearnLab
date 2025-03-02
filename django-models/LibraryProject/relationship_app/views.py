from django.shortcuts import render
from django.views.generic import DetailView, ListView
from relationship_app.models import Book, Library, Author, Librarian 

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    book_list = [f"{book.title} by {book.author.name}" for book in books]
    return render(request, "relationship_app/list_books.html", {"book_list": book_list})

# Implement Class-based View:

# Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
# Utilize Django’s ListView or DetailView to structure this class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books_in_library"] = self.object.books.all()
        return context
