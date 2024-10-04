from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_screen, name='home_screen'), # main screen link
]