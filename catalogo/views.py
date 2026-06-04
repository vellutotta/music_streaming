from django.views.generic import ListView
from .models import Song

# Create your views here.
class SongList(ListView):
    model = Song
    template_name = 'catalogo/song_list.html'
    context_object_name = 'songs'
