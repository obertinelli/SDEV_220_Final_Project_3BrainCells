from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen, name='home_screen'), # main screen link
    path('book/<str:pk>', views.book_details, name="book_details"), #book detail screen
    path('book/new/', views.add_book, name="add_book"),
    path('book/<str:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<str:pk>/remove/', views.book_remove, name='book_remove'),
]