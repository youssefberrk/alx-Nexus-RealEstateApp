from django.urls import path

from .views import ApplicationViewSet, LeaseViewSet, PaymentViewSet

urlpatterns = [
    path('leases/', LeaseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('leases/<int:pk>/', LeaseViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('applications/', ApplicationViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('applications/<int:pk>/', ApplicationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('applications/<int:pk>/update_status/', ApplicationViewSet.as_view({'post': 'update_status'})),
    path('payments/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('payments/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]