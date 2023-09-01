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
