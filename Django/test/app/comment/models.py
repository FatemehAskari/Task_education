from django.db import models
from application.models import *
from person.models import *
# Create your models here.


class comment(models.Model):
    status_choice=(
        ('pending','pending'),
        ('accept','accept'),
        ('reject','reject')
    )
    text=models.CharField(max_length=20)
    person=models.ForeignKey(person,on_delete=models.CASCADE)
    application=models.ForeignKey(application,on_delete=models.CASCADE)
    create_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=status_choice,default='pending')    
    

