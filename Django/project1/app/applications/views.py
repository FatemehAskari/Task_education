from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .forms import *
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.shortcuts import redirect
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import check_password
from django.views import View
# from django.
# Create your views here.

class Login(TemplateView):
    
    def get(self,request):
        login_form=LoginForm()
        context={
            'form':login_form
        }
        return render(request,'login.html',context)
    
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            print("sfdf")
            user_username=form.cleaned_data.get('username')
            user_password=form.cleaned_data.get('password')
            user:person=person.objects.filter(username__iexact=user_username).first()
            
            if user is not None:
                print(user.password,user_password)
                is_correct=user.check_password(user_password)
                print(is_correct)
                if is_correct:
                    login(request,user)
                    return redirect('/')
                else:
                    form.add_error('username','no user with your info')
                    
            else:
                form.add_error('username','no user with your info')
                
        context={
            'form':form
        }
        return render(request,'login.html',context)                    
                                
class Signup(TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SignupForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            user_username=form.cleaned_data.get('username')
            user:bool=person.objects.filter(username__iexact=user_username).exists()
            if user:
                form.add_error('username','username تکراری است')
            else:  
                user_firstname=form.cleaned_data.get('first_name')
                user_lastname=form.cleaned_data.get('last_name')
                user_password=form.cleaned_data.get('password')
                new_person=person(
                    username=user_username,
                    first_name=user_firstname,
                    last_name=user_lastname
                )
                new_person.set_password(user_password)
                new_person.save()
                return redirect('login')
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class AppSearchView(ListView):
    model=application
    template_name='allapp.html'
    context_object_name='applications'
    
    def get_queryset(self):
        app_name=self.request.GET.get('app_name')
        if app_name:
            return application.objects.filter(name__contains=app_name)
        else:
            return application.objects.all()  

class Logout(View):     
    def get(self,request):
        logout(request)
        return redirect('login')
             