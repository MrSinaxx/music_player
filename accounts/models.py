from django.contrib.auth.models import AbstractUser
from django.db import models
from music.models import Song


class CustomUser(AbstractUser):
    ACCOUNT_TYPES = (("V", "VIP"), ("N", "Normal"))
    account_type = models.CharField(choices=ACCOUNT_TYPES, default="N", max_length=1)
    profile_image = models.ImageField(upload_to="users/", blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="likes")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="likes")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "song")

    def __str__(self):
        return f"{self.user.username} liked {self.song.title}"


class Comment(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="comments"
    )
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"Comment by {self.user.username} on {self.song.title}"
