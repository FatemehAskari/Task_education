# Needed imports here
from .models import *
from django.http import HttpResponse

def list_create_tasks(request):
    if request.method == 'GET':
        task_names = Task.objects.all().order_by('name').values_list('name', flat=True)
        response_text = '\n'.join(task_names)
        return HttpResponse(response_text,content_type='text/plain')

def count_tasks(request):
    if request.method == 'GET':
        return HttpResponse(f"You have '{len(Task.objects.all())}' tasks to do",content_type='text/plain') 
