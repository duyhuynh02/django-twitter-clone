from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 


from .models import Tweet


class TwitterListView(LoginRequiredMixin, ListView):
	model = Tweet
	template_name = 'twitter.html'
	login_url = 'login'


class TwitterCreateView(LoginRequiredMixin, CreateView):
	model = Tweet 
	template_name = 'twitter_create.html'
	fields = ['body']
	login_url = 'login'

	def form_valid(self, form):
		form.instance.user = self.request.user 
		return super().form_valid(form)


class TwitterDetailView(LoginRequiredMixin, DetailView):
	model = Tweet 
	template_name = 'twitter_detail.html'
	login_url = 'login'


class TwitterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Tweet 
	template_name = 'twitter_update.html'
	fields = ['body']
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.user == self.request.user


class TwitterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Tweet 
	template_name = 'twitter_delete.html'
	success_url = reverse_lazy('twitter')
	login_url = 'login'

	def test_func(self):
		obj = self.get_object()
		return obj.user == self.request.user
