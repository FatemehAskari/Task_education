from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login , name='login'),
    path('signup/', signup , name='signup'),
    path('',appsearch),
]
