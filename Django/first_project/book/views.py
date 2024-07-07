from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.


def html(request):
    return render(request,'index.html')

def book_detail(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'book_detail.html',{"book":book})

def book_all(request):
    books=Book.objects.all()
    return render(request,'book_all.html',{"books":books})        
    
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
    