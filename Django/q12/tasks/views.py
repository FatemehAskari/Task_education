from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponse

@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        try:
            task=Task.objects.get(id=task_id)
            task_name=task.name
            task.delete()
            return HttpResponse(f"Task Done: '{task_name}'")
        except Task.DoesNotExist:
            return HttpResponse(f"There isn't any task with id '{task_id}'")            
            
                
