from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmViewSet, Film_detailsViewSet, GenreViewSet, TagViewSet, film_details, delete_film

app_name = 'films'

router = DefaultRouter()
router.register(r'film', FilmViewSet, basename='films')
router.register(r'film_details', Film_detailsViewSet, basename='film_details')
router.register(r'genre', GenreViewSet, basename='genres')
router.register(r'tag', TagViewSet, basename='tags')

urlpatterns = [
                  path('', include(router.urls)),
                  path('details/<int:film_id>/', film_details, name='film_details'),
                  path('delete/<int:film_id>/', delete_film, name='delete_film'),
              ] + router.urls
