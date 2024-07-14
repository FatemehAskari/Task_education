from django.urls import path

from library_management import views

urlpatterns = [
    path('booklist/', views.booklist, name='booklist')
]