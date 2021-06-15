from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True


class AccountantPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_accountant is True


class EmployeePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_employee is True


class CookPermissionOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_cook is True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_cook is True


class IsOwnerOrAccountantPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_accountant is True or obj.user == request.user
