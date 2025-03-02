from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
books = Book.objects.filter(author__name=author_name)

# List all books in a library
#
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
