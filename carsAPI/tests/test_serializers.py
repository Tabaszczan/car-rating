"""Test serializers cars API."""
# Standard Library
import json

# Django
from django.test import TestCase
from django.urls import reverse

# 3rd-party
from rest_framework import status
from rest_framework.test import APIRequestFactory

# Local
from ..models import Cars
from ..serializers import CarSerializer
from .factories import CarsFactory


class TestCarSerializer(TestCase):
    """Test for Car serializer."""

    def setUp(self):  # noqa: D102
        self.factory = APIRequestFactory()
        self.car = CarsFactory()
        self.serializer = CarSerializer(instance=self.car)
        self.set_fields = [
            'make_name',
            'model_name',
            'average_rate',
        ]

    def test_contains_expected_fields(self):
        """Test serializer data fields."""
        data = self.serializer.data
        self.assertCountEqual(data.keys(), self.set_fields)

    def test_get_objects(self):
        """Test GET request status and data."""
        CarsFactory()
        CarsFactory()
        CarsFactory()
        CarsFactory()
        response = self.client.get(reverse('cars_list'))
        cars_query = Cars.objects.all()
        serializer = CarSerializer(cars_query, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_object_invalid(self):
        """Test invalid POST Car."""
        car = {
            'make_name': 'No',
            'model_name': 'Name',
        }
        response = self.client.post(
            reverse('cars_list'),
            data=json.dumps(car),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_object_valid(self):
        """Test valid POST Car."""
        car = {
            'make_name': 'honda',
            'model_name': 'civic',
        }
        response = self.client.post(
            reverse('cars_list'),
            data=json.dumps(car),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_object_already_exist(self):
        """Test POST when object already exist."""
        car = {
            'make_name': 'honda',
            'model_name': 'civic',
        }
        response = self.client.post(
            reverse('cars_list'),
            data=json.dumps(car),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(
            reverse('cars_list'),
            data=json.dumps(car),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
