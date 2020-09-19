from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	gender = models.CharField(max_length=20, null=True, blank=True)
	age = models.PositiveIntegerField(null=True, blank=True)
	location = models.CharField(max_length=255)