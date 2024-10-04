from django.shortcuts import render
from .models import Book
# from .Inventory_Class import Inventory

# Create your views here.

# view for home_screen
def home_screen(request):
    books = Book.objects.order_by('title')
    return render(request, 'pages/home_screen.html', {'books': books}) 