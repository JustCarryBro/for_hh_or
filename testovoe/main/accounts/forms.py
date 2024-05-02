from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    your_name = forms.CharField(label='Your name', max_length=100)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
