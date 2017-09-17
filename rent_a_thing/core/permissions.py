from rest_framework import permissions
from rest_framework.compat import is_authenticated

class WriteOnly(permissions.BasePermission):
    
    SAFE_METHODS = ['POST']

    def has_permission(self, request, view):
        if (request.method in ['POST', 'OPTIONS']) or (request.user and is_authenticated(request.user)):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if (request.method in ['POST', 'OPTIONS']) or (request.user and is_authenticated(request.user)):
            return True
        return False
