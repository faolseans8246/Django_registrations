from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomerUserBase(AbstractUser):

    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.username