from django.urls import path, include
from rest_framework.routers import DefaultRouter

from carsAPI import views


urlpatterns = [
    path('cars/', views.CarsList.as_view(), name='cars_list'),
    path('rate/', views.CarRatePostAPIView.as_view(), name='rate_post')
]
