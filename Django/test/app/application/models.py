from django.db import models

# Create your models here.
class application(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)    