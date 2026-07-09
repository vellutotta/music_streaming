from django.urls import path

from .views import (PlaylistListView, PlaylistDetailView, profile_view,
                    PlaylistCreateView, PlaylistUpdateView, PlaylistDeleteView)

urlpatterns = [
    path('', PlaylistListView.as_view(), name='playlist-list'),

    path('<int:pk>/', PlaylistDetailView.as_view(), name='playlist_detail'),

    path('profile/', profile_view, name='user-profile'),

    path('create/', PlaylistCreateView.as_view(), name='playlist-create'),
    path('<int:pk>/edit/', PlaylistUpdateView.as_view(), name='playlist-edit'),
    path('<int:pk>/delete/', PlaylistDeleteView.as_view(), name='playlist-delete'),

]