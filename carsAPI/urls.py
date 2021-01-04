"""Urls carsAPI."""
# Django
from django.urls import path

# Project
from carsAPI import views

urlpatterns = [
    path('cars/', views.CarsList.as_view(), name='cars_list'),
    path('rate/', views.CarRatePostAPIView.as_view(), name='rate_post'),
    path('popular/', views.PopularCarsList.as_view(), name='popular_cars_list'),
]
