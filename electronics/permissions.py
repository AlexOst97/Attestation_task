from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """Доступ к API только активнsым сотрудникам"""

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_active
