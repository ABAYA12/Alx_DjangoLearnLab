from django.contrib import admin
from .models import Book  # Import the Book model

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # Columns shown in the admin list view
    list_filter = ("publication_year", "author")  # Filters for easy navigation
    search_fields = ("title", "author")  # Search functionality

