from django.urls import path
from . import views

urlpatterns = [
    path('brands/', views.list_all_brands, name='list_all_brands'),
    path('mobiles/', views.list_all_mobiles, name='list_all_mobiles'),
    # Define other URLs for the remaining view functions
]