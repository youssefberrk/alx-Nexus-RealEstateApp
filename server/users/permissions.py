from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrAuthenticatedReadOnly(BasePermission):
    """
    - Admins: Can view all users
    - Authenticated users: Can only view their own profile
    - Anyone: Can create an account
    """
    
    def has_permission(self, request, view):
        # Allow account creation (POST request)
        if view.action == 'create':
            return True  # Anyone can register

        # Allow only authenticated users for other requests
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admins can view all users
        if request.user.is_staff:
            return True

        # Regular users can only view their own profile
        return obj == request.user
