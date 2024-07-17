from django import forms
from .models import person
from rest_framework.validators import UniqueValidator
from django.core.exceptions import ValidationError

class SignupForm(forms.ModelForm):
    class Meta:
        model=person
        fields = ['username','password','first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
    # def clean_username(self):
    #     username=self.cleaned_data['username']
    #     if person.objects.filter(username=username).exists():
    #         raise ValidationError("Username already exists.")
    #     return username
            
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)       
            

        
