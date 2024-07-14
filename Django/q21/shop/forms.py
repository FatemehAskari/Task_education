from django import forms

from .models import Person

class PersonalInformation(forms.ModelForm):
    class Meta:
        model=Person
        fields=('full_name','height','gender','age','email','phone','mobile')
    
