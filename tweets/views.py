from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render 

from .forms import CommentForm
from .models import Tweet, Comment


class TwitterListView(ListView):
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

	
def LikeTweetView(request, pk):
	tweet = get_object_or_404(Tweet, pk=request.POST.get('tweet_id'))
	if tweet.likes.filter(id=request.user.id).exists():
		tweet.likes.remove(request.user)
	else: 
		tweet.likes.add(request.user)

	return HttpResponseRedirect(reverse('twitter-detail', args=[str(pk)]))


class TwitterDetailView(LoginRequiredMixin, FormMixin, DetailView):
	model = Tweet 
	template_name = 'twitter_detail.html'
	login_url = 'login'
	form_class = CommentForm

	def get_context_data(self, **kwargs):
		context = super(TwitterDetailView, self).get_context_data(**kwargs)
		tweet = get_object_or_404(Tweet, pk=self.kwargs['pk'])
		total_likes = tweet.total_likes()

		if tweet.likes.filter(id=self.request.user.id).exists():
			liked = True  
		else:
			liked = False

		context['form'] = CommentForm(initial={'post': self.object})
		context['total_likes'] = total_likes
		context['liked'] = liked 

		return context 

	def get_success_url(self):
		return reverse('twitter-detail', kwargs={'pk': self.object.pk})

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		self.object = self.get_object()
		form = self.get_form()

		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user 
		instance.body = self.object 
		instance.save()	
		return super(TwitterDetailView, self).form_valid(form)

	
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

