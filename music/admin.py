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


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("title", "upload_date")
    list_filter = ("upload_date", "artists", "genres")
    search_fields = ("title", "artists__name")
    ordering = ("-upload_date",)
    date_hierarchy = "upload_date"


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "description")
    list_filter = ("owner",)
    search_fields = ("title", "owner__username", "description")
    ordering = ("title",)
