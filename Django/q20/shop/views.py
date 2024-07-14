from django.http import HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from .forms import PersonalInformation
from .models import Person


def show_people(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'show_people.html', context)

# @csrf_exempt
@csrf_protect
def submit_person(request):
    if request.method == 'GET':
        context={}
        context['form']=PersonalInformation()
        return render(request,'new_person.html',context)                        
    elif request.method == 'POST':
        form=PersonalInformation(request.POST)
        if form.is_valid():
            person=Person()
            person.gender=form.cleaned_data['gender']
            person.full_name=form.cleaned_data['full_name']
            person.height=form.cleaned_data['height']
            person.age=form.cleaned_data['age']
            person.save()
            return HttpResponse(person,status=201)