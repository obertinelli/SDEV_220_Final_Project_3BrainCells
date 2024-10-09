from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Book
from .forms import BookForm
# from .Inventory_Class import Inventory

# Create your views here.

# view for home_screen
def home_screen(request):
    books = Book.objects.order_by('title')
    return render(request, 'pages/home_screen.html', {'books': books}) 

# view for book_details
def book_details(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'pages/book_details.html', {'book': book})

# view for add_book - logic to add new books
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('book_details', pk=post.pk)
    else:
        form = BookForm()
    return render(request, 'pages/add_book.html', {'form': form})

# view for edit_book - logic to edit existing book content
def book_edit(request, pk):
    post = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('book_details', pk=post.pk)
    else:
        form = BookForm(instance=post)
    return render(request, 'pages/add_book.html', {'form': form})

def book_remove(request, pk):
    post = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        post.delete()
    return redirect('home_screen')