
# Query all books by a specific author.
from relationship_app.models import Book, Author

def query_books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)

# Query the librarian for a specific library.
from relationship_app.models import Library, Librarian

def query_librarian_by_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

# Query all books in a library.
from relationship_app.models import Library, Book

def query_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return Book.objects.filter(libraries=library)

