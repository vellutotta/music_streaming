

# Register your models here.

from django.contrib import admin
from .models import Playlist, Profile

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):

    list_display = ('name', 'user', 'created_at')

    list_filter = ('user', 'created_at')

    search_fields = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_genre', 'created_at')
    search_fields = ('user__username', 'favorite_genre')
