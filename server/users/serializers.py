from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_staff', 'is_active']
        read_only_fields = ['is_staff', 'is_active']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user