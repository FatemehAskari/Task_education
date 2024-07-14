from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from .models import Musician, Album
from django.views.generic import ListView,DetailView
from django.http import Http404

class MusicianListView(ListView):
    model=Musician
    ordering=['name']
    template_name='musician_list.html'
    paginate_by=1

class AlbumDetailView(DetailView):
    model=Album
    template_name='album_detail.html'
    
    def get_queryset(self):
        return Album.objects.filter(num_stars__gte=3)
        
