from django.urls import path, include


from .views import TwitterView


urlpatterns = [
    path('', TwitterView.as_view(), name='twitter'),

]