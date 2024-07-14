from django.http import HttpResponse
from django.shortcuts import render

from .forms import PersonalInformation
from .models import Person


def show_people(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'show_people.html', context)


# YOU DON'T NEED TO IMPLEMENT THIS FUNCTION
def submit_person(request):
    if request.method == 'GET':
        ...
    elif request.method == 'POST':
        ...
