# Standard Library
import random

# 3rd-party
from factory import LazyAttribute
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory.fuzzy import FuzzyChoice
from factory.fuzzy import FuzzyDecimal

from carsAPI.models import Cars, CarRate


class CarsFactory(DjangoModelFactory):  # noqa: D101
    make_name = Faker('sentence', nb_words=1)
    model_name = Faker('sentence', nb_words=1)

    class Meta:  # noqa: D106
        model = Cars


class CarRateFactory(DjangoModelFactory):  # noqa: D101

    car = SubFactory(CarsFactory)
    rate = FuzzyChoice(dict(CarRate.Rates.choices).keys())

    class Meta:  # noqa: D106
        model = CarRate