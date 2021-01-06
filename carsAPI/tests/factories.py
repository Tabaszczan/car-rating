"""Factories cars API."""
# 3rd-party
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory.fuzzy import FuzzyChoice

# Local
from ..models import CarRate
from ..models import Cars


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
