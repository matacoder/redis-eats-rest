from rest_framework import permissions

from main.services import get_main_switch_status


class MainSwitchPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return get_main_switch_status()


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
