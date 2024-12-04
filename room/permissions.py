from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method not in permissions.SAFE_METHODS:
            return request.user.is_staff
        return True

    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return request.user.is_staff
        return True
