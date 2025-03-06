from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrOwner(BasePermission):
    """
    - Admins: Can view all users
    - Authenticated users: Can only view their own profile
    - Anyone: Can create an account
    """
    
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        if request.user.is_staff:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return obj == request.user
        return obj == request.user or request.user.is_staff
