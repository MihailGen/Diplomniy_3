from django.contrib import admin
from django.urls import path, include
from films import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from users_reviews.views import RegisterView, register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base),
    path('films/', views.films),
    path('', include('films.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('delete/<int:film_id>/', views.delete_film, name='delete_film'),
    path('details/<int:film_id>/', views.film_details, name='film_details'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('register/', register, name='register'),
]
