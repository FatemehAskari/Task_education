from django.db import models
import datetime
# Create your models here.

class Author(models.Model):
    title=models.CharField(max_length=100)   
    
    
class Book(models.Model):
    title=models.CharField(max_length=100)    
    author=models.ManyToManyField(Author)
    release_data=models.DateField(default=datetime.date.today)
    loan_status=models.BooleanField(default=False)

class Library(models.Model):
    number=models.PositiveBigIntegerField()    
    
class Profile(models.Model):
    email=models.EmailField()
    phone_number=models.CharField(max_length=100)
    
class Personal(models.Model):
    class Gender(models.TextChoices):
        MALE='m','Male'
        Female='f','Female'
    gender=models.CharField(max_length=1,choices=Gender.choices,default=Gender.Female)            
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
    library=models.ForeignKey(Library,on_delete=models.CASCADE)

    
        