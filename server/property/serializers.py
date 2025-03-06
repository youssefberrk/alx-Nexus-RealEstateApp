from rest_framework import serializers
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer

User = get_user_model()

from .models import (
    Location, Property
)

class LocationSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)
    
    class Meta:
        model = Location
        fields = ['id', 'address', 'city', 'state', 'country', 'postal_code', 'coordinates', 'latitude', 'longitude']
        read_only_fields = ['coordinates']
    
    def create(self, validated_data):
        latitude = validated_data.pop('latitude')
        longitude = validated_data.pop('longitude')
        validated_data['coordinates'] = Point(longitude, latitude)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'latitude' in validated_data and 'longitude' in validated_data:
            latitude = validated_data.pop('latitude')
            longitude = validated_data.pop('longitude')
            validated_data['coordinates'] = Point(longitude, latitude)
        return super().update(instance, validated_data)


class PropertySerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    manager = UserSerializer()
    tenants = UserSerializer(many=True)

    class Meta:
        model = Property
        fields = [
            'id', 'name', 'price_per_month', 'beds', 'baths', 
            'square_feet', 'property_type', 'posted_date', 
            'average_rating', 'number_of_reviews', 'location_address',
            'manager_name', 'photo_urls'
        ]
