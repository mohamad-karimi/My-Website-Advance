from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    '''
    Create a custom permission class to allow authenticated users
    to access the API, while allowing only the owner or admin
    to modify an object.
    '''

    def has_permission(self, request, view):
        '''
        Check that the user is authenticated before accessing the API.
        '''
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        '''
        Allow read-only requests for all authenticated users.
        For modification requests, allow only the object owner or an admin.
        '''

        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user.is_staff
            or obj.author == request.user
        )