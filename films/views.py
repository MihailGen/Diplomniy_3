from django.shortcuts import render
from rest_framework import viewsets
from films.models import Film, Film_details, Genre, Tag
from films.serializers import FilmSerializer, Film_detailsSerializer, GenreSerializer, TagSerializer


def base(request):
    return render(request, 'films/base.html')

def films(request):
    return render(request, 'films/films.html')

class FilmViewSet(viewsets.ModelViewSet): # Класс-контроллер, для создания набора контроллеров на осное VieSet
    queryset = Film.objects.all() # Набор данных для работы в контроллерах
    serializer_class = FilmSerializer # класс-сериализатор


class Film_detailsViewSet(viewsets.ModelViewSet): # Класс-контроллер, для создания набора контроллеров на осное VieSet
    queryset = Film_details.objects.all() # Набор данных для работы в контроллерах
    serializer_class = Film_detailsSerializer # класс-сериализатор

class GenreViewSet(viewsets.ModelViewSet): # Класс-контроллер, для создания набора контроллеров на осное VieSet
    queryset = Genre.objects.all() # Набор данных для работы в контроллерах
    serializer_class = GenreSerializer # класс-сериализатор

class TagViewSet(viewsets.ModelViewSet): # Класс-контроллер, для создания набора контроллеров на осное VieSet
    queryset = Tag.objects.all() # Набор данных для работы в контроллерах
    serializer_class = TagSerializer # класс-сериализатор