from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerProfileOrReadOnly(BasePermission):
    '''Custom Permission class to check if requesting  user is similar to the object's user field'''
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user