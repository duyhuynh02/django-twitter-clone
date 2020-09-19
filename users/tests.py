from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model 
from django.urls import reverse 


class TwitterPageTests(SimpleTestCase):

	def test_twitter_page_status_code(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_view_url_by_name(self):
		response = self.client.get(reverse('twitter'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('twitter'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'twitter.html')


class RegisterPageTests(TestCase):

	username = 'tester00'
	email = 'tester00@email.com'

	def test_register_page_status_code(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code, 200)

	def test_view_url_by_name(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code, 200)

	def test_view_uses_correct_template(self):
		response = self.client.get(reverse('register'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'register.html')

	def test_register_form(self):
		user = get_user_model().objects.create_user(
				self.username, self.email)
		self.assertEqual(get_user_model().objects.all().count(),1)
		self.assertEqual(get_user_model().objects.all()
						[0].username, self.username)
		self.assertEqual(get_user_model().objects.all()
						[0].email, self.email)


