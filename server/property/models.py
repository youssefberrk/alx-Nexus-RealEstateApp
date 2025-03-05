from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.postgres.fields import ArrayField
from .choices import Amenity, Highlight, PropertyType
from django.contrib.auth import get_user_model


User = get_user_model()

class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    coordinates = gis_models.PointField(srid=4326)
    
    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}"


class Property(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2)
    application_fee = models.DecimalField(max_digits=10, decimal_places=2)
    photo_urls = ArrayField(models.URLField(), blank=True)
    amenities = ArrayField(
        models.CharField(max_length=50, choices=Amenity.choices),
        blank=True
    )
    highlights = ArrayField(
        models.CharField(max_length=50, choices=Highlight.choices),
        blank=True
    )
    is_pets_allowed = models.BooleanField(default=False)
    is_parking_included = models.BooleanField(default=False)
    beds = models.PositiveIntegerField()
    baths = models.DecimalField(max_digits=3, decimal_places=1)
    square_feet = models.PositiveIntegerField()
    property_type = models.CharField(max_length=50, choices=PropertyType.choices)
    posted_date = models.DateTimeField(auto_now_add=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    number_of_reviews = models.PositiveIntegerField(default=0)
    
    # Foreign keys
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='properties')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='managed_properties')
    tenants = models.ManyToManyField(User, related_name='properties', blank=True)
    
    def __str__(self):
        return self.name
