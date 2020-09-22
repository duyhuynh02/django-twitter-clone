from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Tweet(models.Model):
	body = models.CharField(max_length=255, blank=True, null=True)
	user = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.body[:25]

	def get_absolute_url(self):
		return reverse('twitter')
