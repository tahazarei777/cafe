from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15,unique=True, blank=True)

    def __str__(self):
        return self.username