from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}),
            'username': forms.TextInput(attrs={'placeholder': 'Введите ваше имя пользователя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите ваш email'}),
        }