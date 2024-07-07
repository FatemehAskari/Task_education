from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
def appsearch(request, app_name=None):
    if 'app_name' in request.GET:        
        app_name = request.GET['app_name']    
    if app_name:
        applications = application.objects.filter(name__contains=app_name)
    else:
        applications = application.objects.all()
    
    return render(request, 'allapp.html', {'applications': applications})
    
            

    