from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    eth_account_address = models.CharField(max_length=42, unique=True)

    def __str__(self):
        return self.user.username
