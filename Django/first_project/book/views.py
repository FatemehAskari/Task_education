from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.

def start(request):
    return HttpResponse("ddd")

@csrf_exempt
def index(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')  
        try:
            book = Book.objects.get(id=book_id)
            return HttpResponse(f"book request: {book.name}")  
        except Book.DoesNotExist:
            return HttpResponse(
                "<p>"
                  "<b>404</b>"
                "</p>"
                "no book found"
            )
    else:
        return HttpResponse("ddd")
    