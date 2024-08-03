from rest_framework.permissions import BasePermission


class UserWithToken(BasePermission):

    def has_permission(self, request, view):
        print(request)
        print(view)
        return False
