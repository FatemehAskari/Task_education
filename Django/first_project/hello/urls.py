from django.contrib import admin
from django.urls import path
from first_app.views import signup_view
from hello.views import say_hello

urlpatterns = [
    path('<str:first_name>/',say_hello)    
]