from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import (
    Lease, Application, Payment
)
from property.serializers import PropertySerializer
from users.serializers import UserSerializer


class LeaseSerializer(serializers.ModelSerializer):
    property = PropertySerializer()
    tenant = UserSerializer()

    class Meta:
        model = Lease
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    property = PropertySerializer()
    tenant = UserSerializer()
    lease = LeaseSerializer()

    class Meta:
        model = Application
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    lease = LeaseSerializer()
    
    class Meta:
        model = Payment
        fields = '__all__'

