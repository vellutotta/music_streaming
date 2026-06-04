from django.db import models

#Tabelle per genere musicale
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

#Tabelle per canzone
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    audio_file = models.FileField(upload_to='songs/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.artist}"


