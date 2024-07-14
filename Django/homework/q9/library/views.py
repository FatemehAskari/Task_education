from django.http import HttpResponse

from .models import Book
from .render import render_to_readable_output


def book_list(request):
    min_price = request.GET.get('min_price') 
    # Other query parameters
    max_price = request.GET.get('max_price')
    author = request.GET.get('author')
    name = request.GET.get('name')
    
    filters={}
    if min_price:
        filters['price__gte']=min_price   
    if max_price:
        filters['price__lte']=max_price
    if author:
        filters['author__icontains']=author
    if name:
        filters['name__icontains']=name        

    # fill `.filter()` with query parameters
    all_books = Book.objects.filter(**filters)
    
    
    rendered_string = render_to_readable_output(all_books)
    return HttpResponse(rendered_string)
