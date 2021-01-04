from django.contrib import admin

# Register your models here.
from carsAPI.models import Cars, CarRate


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = [
        'make_name',
        'model_name',
    ]
    search_fields = [
        'make_name',
    ]


@admin.register(CarRate)
class CarRateAdmin(admin.ModelAdmin):
    list_display = [
        'car'
    ]
    search_fields = [
        'car'
    ]
