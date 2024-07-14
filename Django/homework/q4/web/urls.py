from django.urls import path

from .views import *

urlpatterns = [
    path('sad/<str:name>/',sad_view),
    path('happy/<str:name>/<int:times>/',happy_view),    
]
