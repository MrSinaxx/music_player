from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(upload_to="artists/")

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist)
    upload_date = models.DateTimeField(auto_now_add=True)
    cover_photo = models.ImageField(upload_to="songs/", blank=True, null=True)
    audio_file = models.FileField(upload_to="songs/")
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
