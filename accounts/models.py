from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=False,null=True)
    email = models.EmailField(unique=True, blank=False)
    def __str__(self):
        return self.username