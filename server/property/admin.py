from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import (
    Location, Property,
)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'state', 'country', 'postal_code')
    search_fields = ('address', 'city', 'state', 'country', 'postal_code')
    list_filter = ('city', 'state', 'country')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_month', 'beds', 'baths', 'property_type', 'location', 'manager')
    list_filter = ('property_type', 'is_pets_allowed', 'is_parking_included', 'beds', 'baths')
    search_fields = ('name', 'description', 'location__address', 'location__city')
