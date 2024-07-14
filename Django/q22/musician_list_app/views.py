from django.shortcuts import render, HttpResponse
from .models import Musician, Album
from django.views import View

class Musician_list(View):
    # type your code here
    def get(self,request):
        artists=Musician.objects.all().order_by('name').values_list('name',flat=True)
        return HttpResponse(artists)