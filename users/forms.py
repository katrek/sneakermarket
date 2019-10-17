from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'country', 'city', 'avatar')


class CustomUserChangeForm(forms.ModelForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ('username',)

