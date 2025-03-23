from django.contrib import admin
from .models import Film, Film_details, Genre, Tag


class Film_detailsInline(admin.StackedInline):
    model = Film_details

class GenreInline(admin.TabularInline):
    model = Genre


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'director')
    search_fields = ('id', 'title', 'director')
    list_filter = ('id', 'title', 'director')

    inlines = [
        Film_detailsInline, GenreInline,
    ]


@admin.register(Film_details)
class Film_detailsAdmin(admin.ModelAdmin):
    list_display = ('year', 'runtime', 'writer', 'actors', 'plot', 'language')
    search_fields = ('year', 'runtime', 'writer', 'actors', 'language')
    list_filter = ('year', 'runtime', 'writer', 'actors', 'language')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'genre')
    search_fields = ('film', 'genre')
    list_filter = ('film', 'genre')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)