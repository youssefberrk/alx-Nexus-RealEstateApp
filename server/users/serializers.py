from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import Group

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'role']



class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']
