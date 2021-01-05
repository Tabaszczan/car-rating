from django.test import TestCase

from carsAPI.tests.factories import CarsFactory, CarRateFactory


class TestCars(TestCase):

    def test_string_representation(self):
        car = CarsFactory()
        self.assertEqual(
            str(car),
            f'{car.make_name} {car.model_name}'
        )

    def test_average_rate_empty(self):
        car = CarsFactory()
        self.assertEqual(car.average_rate, 'No ratings')

    def test_average_rate_not_empty(self):
        car = CarsFactory()
        cr_0 = CarRateFactory(car=car)
        cr_1 = CarRateFactory(car=car)
        cr_2 = CarRateFactory(car=car)
        rate_list = [cr_0.rate, cr_1.rate, cr_2.rate]
        average = round(sum(rate_list) / len(rate_list), 2)
        self.assertEqual(car.average_rate, average)


class TestCarRate(TestCase):
    def test_string_representation(self):
        car_rate = CarRateFactory()
        self.assertEqual(
            str(car_rate),
            f'{car_rate.car}, Rate: {car_rate.get_rate_display()}'
        )
