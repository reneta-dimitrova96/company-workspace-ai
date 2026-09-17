from rest_framework import permissions

from users.models import User


class TicketDetailPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method in ["PUT", "PATCH", "DELETE"] and request.user.role in [
                User.Roles.OWNER, User.Roles.ADMIN]:
            return True

        return False
