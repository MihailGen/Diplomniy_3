from rest_framework import serializers
from .models import User, Reviews, Ratings, Favourites

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ('username', 'password')


# Сериалайзер для Отзывов
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"


# Сериалайзер для Рейтингов
class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = "__all__"


# Сериалайзер для избранных фильмов
class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = "__all__"