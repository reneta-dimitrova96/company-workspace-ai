from rest_framework.permissions import BasePermission

from users.models import User


class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in [User.Roles.OWNER, User.Roles.ADMIN]:
            return True

        return False


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == User.Roles.OWNER:
            return True

        return False
