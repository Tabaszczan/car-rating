from django.db import models


class Cars(models.Model):
    make_name = models.CharField('Car Make Name', max_length=255)
    model_name = models.CharField('Car Model Name', max_length=255)

    def __str__(self):
        return f'{self.make_name} {self.model_name}'

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class CarRate(models.Model):
    class Rates(models.IntegerChoices):
        VERY_BAD = 1
        BAD = 2
        NEUTRAL = 3
        GOOD = 4
        VERY_GOOD = 5

    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='Car')
    rate = models.IntegerField('Rating', choices=Rates.choices)

    def __str__(self):
        return f'{self.car}, Rate: {self.get_rate_display()}'
