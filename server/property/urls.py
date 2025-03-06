from django.urls import path

from .views import PropertyViewSet, LocationViewSet

urlpatterns = [
    path('properties/', PropertyViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('properties/<int:pk>/', PropertyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('locations/', LocationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('locations/<int:pk>/', LocationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
