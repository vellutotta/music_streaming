

# Create your views here.

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Playlist
from .forms import PlaylistForm


class PlaylistListView(LoginRequiredMixin, ListView):
    model = Playlist
    template_name = 'playlists/playlist_list.html'
    context_object_name = 'playlists'

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)


class PlaylistDetailView(LoginRequiredMixin, DetailView):
    model = Playlist
    template_name = 'playlists/playlist_detail.html'
    context_object_name = 'playlist'


@login_required
def profile_view(request):
    profile = getattr(request.user, 'profile', None)

    user_playlists = request.user.playlist_set.all()

    context = {
        'profile': profile,
        'user_playlists': user_playlists
    }
    return render(request, 'playlists/profile.html', context)


class PlaylistCreateView(LoginRequiredMixin, CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlists/playlist_form.html'
    success_url = reverse_lazy('playlist-list')

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)

class PlaylistUpdateView(LoginRequiredMixin, UpdateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlists/playlist_form.html'
    success_url = reverse_lazy('playlist-list')

    def get_queryset(self):

        return Playlist.objects.filter(user=self.request.user)

class PlaylistDeleteView(LoginRequiredMixin, DeleteView):
    model = Playlist
    template_name = 'playlists/playlist_confirm_delete.html'
    success_url = reverse_lazy('playlist-list')

    def get_queryset(self):

        return Playlist.objects.filter(user=self.request.user)