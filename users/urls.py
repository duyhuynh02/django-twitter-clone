from django.urls import path, include

from .views import RegisterView, settings


urlpatterns = [
    path('settings/', settings, name='profile-update'),
    path('', RegisterView.as_view(), name='register'),
]