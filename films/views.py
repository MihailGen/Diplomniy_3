from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import viewsets

from films.models import Film, Film_details, Genre, Tags
from films.serializers import FilmSerializer, Film_detailsSerializer, GenreSerializer, TagSerializer


def base(request):
    return render(request, 'films/base.html')


def films(request):
    film_list = Film.objects.all().order_by('-release_date')
    return render(request, 'films/films.html', {'film_list': film_list})


def film_details(request, film_id):
    film = Film_details.objects.get(id=film_id)
    return render(request, 'films/film_details.html', {'film': film})


def film_list(request):
    film_list = Film.objects.all().order_by('-release_date')
    return render(request, 'films/films.html', {'film_list': film_list})


@require_POST
def delete_film(film_id):
    # film = Film.objects.get(id=film_id)
    film = get_object_or_404(Film, pk=film_id)
    film.delete()
    return redirect('films')


class FilmViewSet(viewsets.ModelViewSet):  # Класс-контроллер, для создания набора контроллеров на осное VieSet
    queryset = Film.objects.all()  # Набор данных для работы в контроллерах
    serializer_class = FilmSerializer  # класс-сериализатор


class Film_detailsViewSet(viewsets.ModelViewSet):  # Класс-контроллер, для создания набора контроллеров на осное VieSet
    queryset = Film_details.objects.all()  # Набор данных для работы в контроллерах
    serializer_class = Film_detailsSerializer  # класс-сериализатор


class GenreViewSet(viewsets.ModelViewSet):  # Класс-контроллер, для создания набора контроллеров на осное VieSet
    queryset = Genre.objects.all()  # Набор данных для работы в контроллерах
    serializer_class = GenreSerializer  # класс-сериализатор


class TagViewSet(viewsets.ModelViewSet):  # Класс-контроллер, для создания набора контроллеров на осное VieSet
    queryset = Tags.objects.all()  # Набор данных для работы в контроллерах
    serializer_class = TagSerializer  # класс-сериализатор
