from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from .models import (
    Location, Property, 
)
from .serializers import (
    LocationSerializer, PropertySerializer
)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['city', 'state', 'country', 'postal_code']
    search_fields = ['address', 'city', 'state', 'country']


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['property_type', 'beds', 'is_pets_allowed', 'is_parking_included']
    search_fields = ['name', 'description', 'location__city', 'location__state']
    ordering_fields = ['price_per_month', 'posted_date', 'average_rating']

    
    @action(detail=False, methods=['get'])
    def nearby(self, request):
        """Find properties near a specific location"""
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        distance = request.query_params.get('distance', 10)  # Default 10km
        
        if not latitude or not longitude:
            return Response(
                {'error': 'Latitude and longitude are required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            point = Point(float(longitude), float(latitude), srid=4326)
            queryset = Property.objects.filter(
                location__coordinates__distance_lte=(point, D(km=float(distance)))
            ).annotate(
                distance=Distance('location__coordinates', point)
            ).order_by('distance')
            
            serializer = PropertySerializer(queryset, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response(
                {'error': 'Invalid coordinates or distance'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
