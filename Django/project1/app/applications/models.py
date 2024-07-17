from django.db import models

from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

# Create your models here.
class application(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)    
    image = models.ImageField(upload_to='static/', null=True, blank=True)

    # def __str__(self):
    #     return self.name

class person(AbstractUser):
    username=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=100)        
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    # def __str__(self):
    #     return self.username


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
