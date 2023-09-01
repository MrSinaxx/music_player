from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200, unique=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="artists/images/", null=True, blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist, related_name="songs")
    upload_date = models.DateTimeField(auto_now_add=True)
    cover_photo = models.ImageField(
        upload_to="songs/cover_photos/", null=True, blank=True
    )
    audio_file = models.FileField(upload_to="songs/audio_files/")
    genres = models.ManyToManyField(Genre, related_name="songs")

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="playlists"
    )
    songs = models.ManyToManyField(Song, related_name="playlists")

    def __str__(self):
        return self.title
