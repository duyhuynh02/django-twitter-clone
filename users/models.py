from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from PIL import Image


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=255)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

    @property 
    def followers(self):
        return Follow.objects.filter(follower_id=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user_id=self.user).count()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300: 
            img.thumbnail((300,300))
            img.save(self.image.path)


class Follow(models.Model):
    user = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
        related_name="following",
    )
    follower = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="followers",
    )

    def __str__(self):
        return f'{self.user} followed {self.follower}'

