from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """ This model is used for the add user details"""
    username = None
    email = models.EmailField(null=True, blank=True, unique=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to="profile/", blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
