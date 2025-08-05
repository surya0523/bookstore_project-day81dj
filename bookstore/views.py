from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Book, Author, Category

# existing views from the project
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

# Login/Register views you recently added
def register(request):
    # ... your register view code ...
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created.')
            return redirect('book_list')
        else:
            messages.error(request, 'Registration failed. Please check the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'bookstore/register.html', {'form': form})

def user_login(request):
    # ... your login view code ...
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}.')
                return redirect('book_list')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    form = AuthenticationForm()
    return render(request, 'bookstore/login.html', {'form': form})

def user_logout(request):
    # ... your logout view code ...
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('book_list')