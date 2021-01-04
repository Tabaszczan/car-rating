from rest_framework import serializers

from carsAPI.models import Cars, CarRate


class CarSerializer(serializers.Serializer):
    make_name = serializers.CharField(required=True, max_length=255)
    model_name = serializers.CharField(required=True, max_length=255)

    def create(self, validated_data):
        car, created = Cars.objects.get_or_create(**validated_data)
        if created:
            return car
        else:
            error = {"message": "Car already exist in database!"}
            raise serializers.ValidationError(error)

    def update(self, instance, validated_data):
        pass


class CarRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRate
        fields = ['car', 'rate']
