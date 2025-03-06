from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import (
    UserSerializer
)
from .models import CustomUser as User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .permissions import IsAdminOrOwner


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrOwner]

    def get_permissions(self):
        if self.action == 'create':  # Allow anyone to register
            return [AllowAny()]
        if self.action == 'update' or self.action == 'partial_update':  # Allow only admins and owners to update
            return [IsAdminOrOwner]
        return [IsAdminUser]  # Admins can do everything

    def get_queryset(self):
        if self.request.user.is_staff:  # Admins can see all users
            return User.objects.all()
        return User.objects.filter(id=self.request.user.id)  # Regular users see only themselves

    def create(self, request, *args, **kwargs):
        """ Override create to properly hash the password """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])  # Hash the password
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """ Override update to properly hash the password """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)