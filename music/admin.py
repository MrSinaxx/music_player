from django.contrib import admin
from .models import Genre, Artist, Song, Playlist


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name", "bio")
    search_fields = ("name", "bio")
    ordering = ("name",)
