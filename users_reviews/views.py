from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny

from films.views import films
from .forms import *
from .forms import UserRegisterForm
from .models import User
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect(films)
    else:
        form = UserRegisterForm()
    return render(request, 'users_reviews/register.html', {'form': form})


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
