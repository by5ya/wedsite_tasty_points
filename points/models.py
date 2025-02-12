from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    email = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.username