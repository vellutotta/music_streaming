

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from catalogo.models import Song


class Playlist(models.Model):

    name = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE)


    songs = models.ManyToManyField(Song, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - di {self.user.username}"

class Profile(models.Model):

        user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


        bio = models.TextField(max_length=300, blank=True, verbose_name="Biografia")
        favorite_genre = models.CharField(max_length=100, blank=True, verbose_name="Genere Preferito")
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Profilo di {self.user.username}"


