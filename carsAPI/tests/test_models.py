"""Test models cars API."""
# Django
from django.test import TestCase

# Project
from carsAPI.tests.factories import CarRateFactory
from carsAPI.tests.factories import CarsFactory


class TestCars(TestCase):
    """Test Car model."""

    def test_string_representation(self):
        """Test if model has valid string representation."""
        car = CarsFactory()
        self.assertEqual(
            str(car),
            f'{car.make_name} {car.model_name}',
        )

    def test_average_rate_empty(self):
        """Test average rate for car without ratings."""
        car = CarsFactory()
        self.assertEqual(car.average_rate, 'No ratings')

    def test_average_rate_not_empty(self):
        """Test average rate for car with ratings."""
        car = CarsFactory()
        cr_0 = CarRateFactory(car=car)
        cr_1 = CarRateFactory(car=car)
        cr_2 = CarRateFactory(car=car)
        rate_list = [cr_0.rate, cr_1.rate, cr_2.rate]
        average = round(sum(rate_list) / len(rate_list), 2)
        self.assertEqual(car.average_rate, average)


class TestCarRate(TestCase):
    """Test Car rate model."""

    def test_string_representation(self):
        """Test if model has valid string representation."""
        car_rate = CarRateFactory()
        self.assertEqual(
            str(car_rate),
            f'{car_rate.car}, Rate: {car_rate.get_rate_display()}',
        )
