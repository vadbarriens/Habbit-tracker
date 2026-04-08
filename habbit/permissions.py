from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwner(permissions.BasePermission):
    """Позволяет доступ только владельцу объекта"""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsPublicOrOwner(BasePermission):
    """Позволяет просмотр публичных привычек всем, но редактирование только владельцу"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.is_public or obj.owner == request.user
        return obj.owner == request.user
