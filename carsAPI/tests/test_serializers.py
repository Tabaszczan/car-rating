import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory

from carsAPI.models import Cars
from carsAPI.serializers import CarSerializer
from carsAPI.tests.factories import CarsFactory


class TestCarSerializer(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.car = CarsFactory()
        self.serializer = CarSerializer(instance=self.car)
        self.set_fields = [
            'make_name',
            'model_name',
            'average_rate',
        ]

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertCountEqual(data.keys(), self.set_fields)

    def test_get_objects(self):
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



