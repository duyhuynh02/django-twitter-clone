from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Tweet

class TweetTests(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username='testuser',
			email='test@email.com',
			password='specialpassword'
		)

		self.tweet = Tweet.objects.create(
			body='Test tweet!',
			user=self.user,
		)


	def test_tweet_string_representation(self):
		tweet = Tweet(body='Great content.')
		self.assertEqual(str(tweet), tweet.body)


	def test_tweet_content(self):
		self.assertEqual(f'{self.tweet.user}','testuser')
		self.assertEqual(f'{self.tweet.body}', 'Test tweet!')


	def test_tweet_list_view(self):
		response = self.client.get(reverse('twitter'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Test tweet!')
		self.assertTemplateUsed(response, 'twitter.html')


	def test_tweet_detail_view(self):
		response = self.client.get('/tweets/1/')
		no_response = self.client.get('/tweets/100000/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'Test tweet!')
		self.assertTemplateUsed(response, 'twitter_detail.html')
