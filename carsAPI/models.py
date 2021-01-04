"""Models carsAPI."""
# Django
from django.db import models
from django.db.models import Avg


class Cars(models.Model):
    """Cars model."""

    make_name = models.CharField('Car Make Name', max_length=255)
    model_name = models.CharField('Car Model Name', max_length=255)

    def __str__(self):  # noqa: D105
        return f'{self.make_name} {self.model_name}'

    @property
    def average_rate(self):
        """Property shows average rate for cars, no ratings if there is no rates."""
        ratings = CarRate.objects.filter(car=self).aggregate(Avg('rate'))
        return round(ratings['rate__avg'], 2) if ratings['rate__avg'] else 'No ratings'

    class Meta:  # noqa: D106
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class CarRate(models.Model):
    """Car rate model."""

    class Rates(models.IntegerChoices):
        """Rate choices."""

        VERY_BAD = 1
        BAD = 2
        NEUTRAL = 3
        GOOD = 4
        VERY_GOOD = 5

    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='Car')
    rate = models.IntegerField('Rating', choices=Rates.choices, default=Rates.NEUTRAL)

    def __str__(self):  # noqa: D105
        return f'{self.car}, Rate: {self.get_rate_display()}'

    class Meta:  # noqa: D106
        verbose_name = 'Car rate'
        verbose_name_plural = 'Cars ratings'
