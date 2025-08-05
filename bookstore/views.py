from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Category

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookstore/book_detail.html', {'book': book})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.books.all()
    return render(request, 'bookstore/author_detail.html', {'author': author, 'books': books})
    
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    books = category.book_set.all()
    return render(request, 'bookstore/category_detail.html', {'category': category, 'books': books})