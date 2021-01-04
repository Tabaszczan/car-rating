from rest_framework import serializers

from carsAPI.models import Cars, CarRate


class CarSerializer(serializers.ModelSerializer):
    # average_rate = serializers.SerializerMethodField('average_value')

    # def average_value(self):
    #     pass

    def create(self, validated_data):
        car, created = Cars.objects.get_or_create(**validated_data)
        if created:
            return car
        else:
            error = {"message": "Car already exist in database!"}
            raise serializers.ValidationError(error)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Cars
        fields = ['make_name', 'model_name', 'average_rate']


class CarRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRate
        fields = ['car', 'rate']
