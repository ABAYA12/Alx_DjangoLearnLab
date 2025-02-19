# Update Operation

## Command:
```python
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(f"Updated Title: {book_to_update.title}")  # Ensure "book.title" appears
```

## Output:
```
(Paste your actual output here)
```
