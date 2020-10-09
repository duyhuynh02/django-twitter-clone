from django.urls import path, include

from .views import (
    TwitterCreateView, 
    TwitterListView, 
    TwitterDetailView,
    TwitterUpdateView,
    TwitterDeleteView,

    LikeTweetView,
)


urlpatterns = [
    path('tweets/new/', TwitterCreateView.as_view(), name='twitter-create'),
    path('tweets/<int:pk>/', TwitterDetailView.as_view(), name='twitter-detail'),
    path('tweets/<int:pk>/liked', LikeTweetView, name='like_post'),
    path('tweets/<int:pk>/update/', TwitterUpdateView.as_view(), name='twitter-update'),
    path('tweets/<int:pk>/delete/', TwitterDeleteView.as_view(), name='twitter-delete'),
    path('', TwitterListView.as_view(), name='twitter'),

]