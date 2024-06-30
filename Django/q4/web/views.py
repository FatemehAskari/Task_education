from django.http import HttpResponse

def sad_view(request,name):
    return HttpResponse(f"Nobody likes you, {name}!")

def happy_view(request,name,times):
    return HttpResponse(f"You are great, {name} :)<br>"* times)
    
    
