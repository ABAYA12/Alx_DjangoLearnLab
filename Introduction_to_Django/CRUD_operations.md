# CRUD Operations in Django Shell

## Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
```
### Output:
```
(Paste your actual output here)
```

## Retrieve
```python
retrieved_book = Book.objects.get(title="1984")
print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Year: {retrieved_book.publication_year}")
```
### Output:
```
(Paste your actual output here)
```

## Update
```python
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(Book.objects.get(id=book_to_update.id))
```
### Output:
```
(Paste your actual output here)
```

## Delete
```python
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()
print(Book.objects.all())
```
### Output:
```
(Paste your actual output here)
```
