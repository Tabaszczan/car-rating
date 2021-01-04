from django.db import models


class Cars(models.Model):
    make_name = models.CharField('Car Make Name', max_length=255)
    model_name = models.CharField('Car Model Name', max_length=255)

    def __str__(self):
        return f'{self.make_name} - {self.model_name}'