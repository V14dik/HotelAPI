from rest_framework import permissions


class IsOwnerOrAdminBookingPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS) or request.method == "DELETE":
            return bool(request.user.is_staff or (request.user.id is obj.user.id))

        return request.user.is_staff
