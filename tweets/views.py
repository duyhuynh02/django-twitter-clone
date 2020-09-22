from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 

from .models import Tweet


class TwitterListView(ListView):
	model = Tweet
	template_name = 'twitter.html'


class TwitterCreateView(CreateView):
	model = Tweet 
	template_name = 'twitter_create.html'
	fields = ['user', 'body']


class TwitterDetailView(DetailView):
	model = Tweet 
	template_name = 'twitter_detail.html'


class TwitterUpdateView(UpdateView):
	model = Tweet 
	template_name = 'twitter_update.html'
	fields = ['body']


class TwitterDeleteView(DeleteView):
	model = Tweet 
	template_name = 'twitter_delete.html'
	success_url = reverse_lazy('twitter')

