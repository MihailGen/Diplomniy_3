from django.contrib import admin
from django.urls import path, include
from films import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from users_reviews.views import (RegisterView, register, reviews_create, ReviewsListView, ReviewsRetrievView,
                                 ReviewsUpdateView, ReviewsDestroyView)


urlpatterns = [
    #path('users/', include('users_reviews.urls')),
    path('admin/', admin.site.urls),
    path('base/', views.base),
    path('films/', views.film_list, name='films_list'),
    #path('films/', views.films),
    path('', include('films.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('delete/<int:film_id>/', views.delete_film, name='delete_film'),
    path('details/<int:film_id>/', views.film_details, name='film_details'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('register/', register, name='register'),

    path('', include('users_reviews.urls')),
    path('reviews_create/', reviews_create, name='reviews_create'),
    #path('reviews/create/', ReviewsCreateView.as_view(), name='reviews-create'),
    path('reviews/', ReviewsListView.as_view(), name='comment-list'),
    path('reviews/<int:pk>/', ReviewsRetrievView.as_view(), name='comment-retrieve'),
    path('reviews/<int:pk>/update/', ReviewsUpdateView.as_view(), name='comment-update'),
    path('reviews/<int:pk>/delete/', ReviewsDestroyView.as_view(), name='comment-destroy'),



]
