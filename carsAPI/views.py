import requests
from django.db.models import Avg
from django.shortcuts import render
from rest_framework import viewsets, status
# Create your views here.
from rest_framework.response import Response

from carsAPI.models import Cars, CarRate
from carsAPI.serializers import CarSerializer, CarRateSerializer
from rest_framework import generics


class CarsList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        rating = CarRate.objects.filter(car__in=queryset).aggregate(Avg('rate'))
        print(rating)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        if request.method == 'POST':
            make_name = validated_data.get('make_name')
            model_name = validated_data.get('model_name')
            r = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make_name}?format=json',
                             timeout=10)
            if r.status_code == 200:
                data = r.json()['Results']
                for item in data:
                    if item['Make_Name'] == make_name and item['Model_Name'] == model_name:
                        self.perform_create(serializer)
                        headers = self.get_success_headers(serializer.data)
                        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
                return Response({"message": "Car doesn't exist."}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"message": "Request failed."}, status=r.status_code)
        else:
            return Response({"message": "Method is not allowed."}, status=status.HTTP_400_BAD_REQUEST)


class CarRatePostAPIView(generics.ListCreateAPIView):
    queryset = CarRate.objects.all()
    serializer_class = CarRateSerializer
    permission_classes = []
