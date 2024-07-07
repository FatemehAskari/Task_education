from django.db import models

# Create your models here.
class application(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)    
    image = models.ImageField(upload_to='static/', null=True, blank=True)

    def __str__(self):
        return self.name

class person(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)        
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)


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
    
            