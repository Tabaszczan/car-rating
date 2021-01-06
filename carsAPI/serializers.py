"""Serializers carsAPI."""
# 3rd-party
from rest_framework import serializers

# Local
from .models import CarRate
from .models import Cars


class CarSerializer(serializers.ModelSerializer):
    """Serializer for Car."""

    def create(self, validated_data):
        """Create method check if object in base already exist."""
        car, created = Cars.objects.get_or_create(**validated_data)
        if created:
            return car
        else:
            error = {'message': 'Car already exist in database!'}
            raise serializers.ValidationError(error)

    class Meta:  # noqa: D106
        model = Cars
        fields = ['make_name', 'model_name', 'average_rate']


class CarRateSerializer(serializers.ModelSerializer):
    """Serializer for car rate."""

    class Meta:  # noqa: D106
        model = CarRate
        fields = ['car', 'rate']
