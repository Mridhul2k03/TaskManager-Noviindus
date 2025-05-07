from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsSuperAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'superadmin'

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'user'

class IsAdminOrSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin' or request.user.role == 'superadmin'