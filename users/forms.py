from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'gender', 'email', 'age', 'location',]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'gender', 'email', 'age', 'location',]


class CustomUserUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile 
        fields = ['image', 'bio']





