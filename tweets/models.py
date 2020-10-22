from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from users.models import CustomUser


class Tweet(models.Model):
    body = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(CustomUser, related_name='tweet_likes')

    def __str__(self):
        return self.body[:25]

    def total_likes(self):
        return self.likes.count()

    @property
    def number_of_comments(self):
        return Comment.objects.filter(tweet=self).count()

    def get_absolute_url(self):
        return reverse('twitter')


class Comment(models.Model):
    tweet = models.ForeignKey(
        Tweet, 
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('twitter-detail', args=[str(pk)])


