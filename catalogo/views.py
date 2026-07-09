from django.views.generic import ListView
from .models import Song
from django.db.models import Q



class SongList(ListView):
    model = Song
    template_name = 'catalogo/song_list.html'
    context_object_name = 'songs'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)


        query = self.request.GET.get('q', '')


        if query:
            context['search_results'] = Song.objects.filter(
                Q(title__icontains=query) | Q(artist__icontains=query)
            ).distinct()
        else:
            context['search_results'] = None


        context['query'] = query

        return context