from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('signup/', Signup.as_view() , name='signup'),
    path('',AppSearchView.as_view(), name='app_search'),
    path('logout/', Logout.as_view(), name='logout'),
]
