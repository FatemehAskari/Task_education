from .models import Book
from django.shortcuts import render


def booklist(request):
    ketabha=Book.objects.all()
    context=context = {'books': ketabha}
    return render(request,'booklist.html',context)
