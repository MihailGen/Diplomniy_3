from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Film, Ratings, Reviews


class AuthenticatedAPITests(TestCase):

    def setUp(self):
        self.film = Film.objects.create(title="Annie Hall", director="Woody Allen", release_date="1977-04-20")
        User = get_user_model()
        self.user = User.objects.create_superuser(password='testuser', email="user@inbox.ru")
        self.client.login(password='testuser', email="user@inbox.ru")
        self.reviews = Reviews.objects.create(film=self.film, user=self.user, reviews_body='Очень хороший фильм!!!')
        self.ratings = Ratings.objects.create(film=self.film, user=self.user, rating='1')

    def test_authenticated_access(self):
        url = reverse('register')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rating_create(self):
        url = reverse('rating_create', args=[self.film.pk])
        data = dict(film=self.film, user='1', rating='1')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_reviews_create(self):
        url = reverse('reviews_create', args=[self.film.pk])
        print(url)
        data = dict(film=self.film, user='1', reviews_body='Очень, ну очень хороший фильм!!!')
        print(data)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def tearDown(self):
        # очистка лишних данных после выполнения тестов
        Reviews.objects.all().delete()
        Ratings.objects.all().delete()
        Film.objects.all().delete()
