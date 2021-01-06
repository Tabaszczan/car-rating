"""Views carsAPI."""
# Django
from django.db.models import Count

# 3rd-party
import requests
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Local
from .models import CarRate
from .models import Cars
from .serializers import CarRateSerializer
from .serializers import CarSerializer


@api_view(['GET'])
def api_root(request, format=None):
    """View for links to endpoints."""
    return Response({
        'cars': reverse('cars_list', request=request, format=format),
        'rates': reverse('rate_post', request=request, format=format),
        'popular': reverse('popular_cars_list', request=request, format=format),
    })


class CarsList(generics.ListCreateAPIView):
    """List with create view for cars."""

    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        """Create car method from external API."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        if request.method == 'POST':
            make_name = validated_data.get('make_name')
            model_name = validated_data.get('model_name')
            r = requests.get(
                f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/'
                f'{make_name}?format=json',
                timeout=10,
            )
            if r.status_code == 200:
                data = r.json()['Results']
                for item in data:
                    if item['Make_Name'].upper() == make_name.upper() and \
                            item['Model_Name'].upper() == model_name.upper():
                        serializer.validated_data['make_name'] = item['Make_Name']
                        serializer.validated_data['model_name'] = item['Model_Name']
                        self.perform_create(serializer)
                        headers = self.get_success_headers(serializer.data)
                        return Response(
                            serializer.data,
                            status=status.HTTP_201_CREATED,
                            headers=headers,
                        )
                return Response(
                    {'message': "Car doesn't exist."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            else:
                return Response({'message': 'Request failed.'}, status=r.status_code)
        else:
            return Response(
                {'message': 'Method is not allowed.'},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CarRatePostAPIView(generics.CreateAPIView):
    """Create view for adding car rate."""

    queryset = CarRate.objects.all()
    serializer_class = CarRateSerializer
    permission_classes = []


class PopularCarsList(generics.ListAPIView):
    """List view order by most popular cars."""

    queryset = Cars.objects.annotate(
        num_carrate=Count('Car', distinct=True),
    ).order_by('-num_carrate')
    serializer_class = CarSerializer
    permission_classes = []
