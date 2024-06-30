from django.db import models

# Create your models here.

class Author(models.Model):
    title=models.CharField(max_length=100)   
    
    
class Book(models.Model):
    title=models.CharField(max_length=100)    
    author=models.ManyToManyField(Author)

class Library(models.Model):
    number=models.PositiveBigIntegerField()    
    
class Profile(models.Model):
    email=models.EmailField()
    phone_number=models.CharField(max_length=100)
    
class Personal(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
    library=models.ForeignKey(Library,on_delete=models.CASCADE)

    
        