from django.urls import path
from .views import *

urlpatterns = [
    path('books/',index),
    path('books/ss',html),
    path('book/<int:book_id>/',book_detail),
    path('book/',book_all)
]
