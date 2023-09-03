from django.contrib import admin
from .models import CustomUser, Like, Comment


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "account_type", "date_joined", "last_login")
    list_filter = ("account_type", "is_staff", "date_joined")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("-date_joined",)
    date_hierarchy = "date_joined"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "song", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("user__username", "song__title")
    ordering = ("-timestamp",)
    date_hierarchy = "timestamp"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "song", "text", "timestamp", "approved")
    list_filter = ("approved", "timestamp")
    search_fields = ("user__username", "song__title", "text")
    ordering = ("-timestamp",)
    date_hierarchy = "timestamp"
