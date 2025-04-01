from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.permissions import AllowAny

from films.views import films
from .forms import *
from .forms import UserRegisterForm
from .models import Reviews, Ratings
from .serializers import RegisterSerializer, ReviewsSerializer, RatingsSerializer

User = get_user_model()


def reviews_create(request):
    reviews = Reviews.objects.create(film=request.film_id, user=request.user)
    reviews.save()
    return render(request, 'films/film_details.html', {'film': request.film_id})


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


@login_required
def profile_page(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'users_reviews/profile.html', {'form': form})


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ReviewsListView(generics.ListAPIView):
    # Класс-контроллер для просомтра списка объектов модели Reviews
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class ReviewsRetrievView(generics.RetrieveAPIView):
    # Класс-контроллер для просмотра отдельного объекта модели Reviews
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class ReviewsUpdateView(generics.UpdateAPIView):
    # Класс-контроллер для редактирования объектов модели Reviews
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class ReviewsDestroyView(generics.DestroyAPIView):
    # Класс-контроллер для удаления объектов модели Reviews
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


# Ratings Views
class RatingsCreateView(generics.CreateAPIView):
    # Класс-контроллер для создани объектов модели Ratings
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


class RatingsListView(generics.ListAPIView):
    # Класс-контроллер для просомтра списка объектов модели Ratings
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


class RatingsRetrievView(generics.RetrieveAPIView):
    # Класс-контроллер для просмотра отдельного объекта модели Ratings
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


class RatingsUpdateView(generics.UpdateAPIView):
    # Класс-контроллер для редактирования объектов модели Ratings
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer


class RatingsDestroyView(generics.DestroyAPIView):
    # Класс-контроллер для удаления объектов модели Ratings
    queryset = Ratings.objects.all()
    serializer_class = RatingsSerializer
