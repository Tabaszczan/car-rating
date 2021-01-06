"""Urls carsAPI."""
# Django
from django.urls import path

# Local
from .views import CarRatePostAPIView
from .views import CarsList
from .views import PopularCarsList
from .views import api_root

urlpatterns = [
    path('', api_root),
    path('cars/', CarsList.as_view(), name='cars_list'),
    path('rate/', CarRatePostAPIView.as_view(), name='rate_post'),
    path('popular/', PopularCarsList.as_view(), name='popular_cars_list'),
]
