from django.contrib import admin
from django.urls import path, include

from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base),
    path('films/', views.films),
    path('', include('films.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('delete/<int:film_id>/', views.delete_film, name='delete_film'),
    path('details/<int:film_id>/', views.film_details, name='film_details'),
]
