from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.

def say_hello(request,first_name):
    return HttpResponse('hello '+ first_name)



