from django.contrib.auth.models import AbstractUser
from django.db import models
from sneakers.models import Sneakers


class CustomUser(AbstractUser):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    sneakers_list = models.ForeignKey(Sneakers, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='/no_avatar.png')


    def __str__(self):
        return self.username


