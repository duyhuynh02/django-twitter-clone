from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView, FormView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse_lazy, reverse

from .forms import CommentForm
from .models import Tweet, Comment

from users.models import CustomUser, Follow  


class TwitterListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'twitter.html'
    login_url = 'login'
    ordering = ['-created_at']
    context_object_name = 'tweets_list'
    paginate_by = 4

    def get_queryset(self):
        user = self.request.user 
        following_user = [user]
        queryset = Follow.objects.filter(user=user)
        for obj in queryset:
            following_user.append(obj.follower)
        return Tweet.objects.filter(user__in=following_user).order_by('-created_at')


class UserTweetListView(TwitterListView):
    template_name = 'user_newsfeed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actual_user = get_object_or_404(CustomUser, username=self.kwargs.get('username'))
        context['actual_user'] = actual_user
        return context


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

    def get_success_url(self):
        return reverse('twitter-detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user 
        instance.tweet = self.object
        instance.save()     
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tweet = get_object_or_404(Tweet, pk=self.kwargs['pk'])
        if tweet.likes.filter(id=self.request.user.id).exists():
            liked = True  
        else:
            liked = False
            
        context['form'] = CommentForm()
        context['total_likes'] = tweet.total_likes
        context['liked'] = liked 
        return context 


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


class UserFollowingView(ListView):
    model = Follow 
    template_name = 'user_follow.html'
    context_object_name = 'follows'

    def get_queryset(self):
        self.user = get_object_or_404(CustomUser, username=self.kwargs['username'])
        return Follow.objects.filter(user=self.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['follow'] = 'following'
        return context 


class UserFollowerView(ListView):
    model = Follow 
    template_name = 'user_follow.html'
    context_object_name = 'follows'

    def get_queryset(self):
        self.follower = get_object_or_404(CustomUser, username=self.kwargs['username'])
        return Follow.objects.filter(follower=self.follower)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['follow'] = 'followers'
        return context 



