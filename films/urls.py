from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmViewSet, Film_detailsViewSet, GenreViewSet, TagViewSet

app_name = 'films'

router = DefaultRouter()
router.register(r'film', FilmViewSet, basename='films')
router.register(r'film_details', Film_detailsViewSet, basename='film_details')
router.register(r'genre', GenreViewSet, basename='genres')
router.register(r'tag', TagViewSet, basename='tags')

urlpatterns = [
                  path('', include(router.urls)),
              ] + router.urls
