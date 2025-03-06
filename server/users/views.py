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
from .permissions import IsAdminOrAuthenticatedReadOnly



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        if self.action in ['create']:  # Allow anyone to register
            return [AllowAny()]
        return [IsAdminOrAuthenticatedReadOnly()]
