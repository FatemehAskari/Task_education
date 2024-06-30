from django.db import models

# Create your models here.
class Person(models.Model):
    GENDER_CHOICES = (
        ("m", "male"),
        ("f", "female"),
    )
    name=models.CharField(max_length=10)
    age=models.EmailField()
    country=models.DateTimeField()
