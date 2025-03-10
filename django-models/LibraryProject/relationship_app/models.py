from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100) 
class Book(models.Model):
    tittle = models.CharField(max_length=100, default='No Title')
    author = models.ManyToManyField(Author, max_length=100)
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, max_length=100)
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, max_length=100)


