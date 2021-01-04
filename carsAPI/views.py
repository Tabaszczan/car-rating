import string

import requests
from django.db.models import Avg, Count
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
                    if item['Make_Name'].upper() == make_name.upper() and \
                            item['Model_Name'].upper() == model_name.upper():
                        serializer.validated_data['make_name'] = item['Make_Name']
                        serializer.validated_data['model_name'] = item['Model_Name']
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


class PopularCarsList(generics.ListAPIView):
    queryset = Cars.objects.annotate(num_carrate=Count('Car', distinct=True)).order_by('-num_carrate')
    serializer_class = CarSerializer
    permission_classes = []

