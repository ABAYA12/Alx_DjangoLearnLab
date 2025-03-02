# Delete Operation

## Command:
```python
from bookshelf.models import Book  # Import Book model

book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")  
book_to_delete.delete()  # Delete the book  
print(Book.objects.all())  # Should return an empty queryset
```

## Output:
```
[]
```
