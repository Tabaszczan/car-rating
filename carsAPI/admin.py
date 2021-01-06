"""Admin carsAPI."""
# Django
from django.contrib import admin

# Local
from .models import CarRate
from .models import Cars


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    """Admin view for cars."""

    list_display = [
        'make_name',
        'model_name',
    ]
    search_fields = [
        'make_name',
    ]


@admin.register(CarRate)
class CarRateAdmin(admin.ModelAdmin):
    """Admin view for car rate."""

    list_display = [
        'car',
    ]
    search_fields = [
        'car',
    ]
