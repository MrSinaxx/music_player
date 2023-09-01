from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ACCOUNT_TYPES = (("VIP", "VIP"), ("NORMAL", "Normal"))
    account_type = models.CharField(
        choices=ACCOUNT_TYPES, default="NORMAL", max_length=10
    )
    profile_image = models.ImageField(upload_to="users/", blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ForeignKey("music.Song", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "song")

    def __str__(self):
        return f"{self.user.username} liked {self.song.title}"


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    song = models.ForeignKey("music.Song", on_delete=models.CASCADE)
    text = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.song.title}"
