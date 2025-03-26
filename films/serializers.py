from rest_framework import serializers
from films.models import Film, Film_details, Genre, Tags

class FilmSerializer(serializers.ModelSerializer): # создаем класс наследник от базового класса сериализатор на основе модели
    class Meta:
        model = Film # модель, для которой будут сериализоваться и десериализоваться данные
        fields = "__all__" # сериализуем все поля

class Film_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film_details
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"