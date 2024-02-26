from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Custom permission to only allow owners to access the view."""

    def has_permission(self, request, view):
        """

        :param request:
        :param view:

        """
        return request.user.role == "owner"


class IsTenant(BasePermission):
    """Custom permission to only allow tenants to access the view."""

    def has_permission(self, request, view):
        """

        :param request:
        :param view:

        """
        return request.user.role == "tenant"


class IsAgent(BasePermission):
    """Custom permission to only allow agents to access the view."""

    def has_permission(self, request, view):
        """

        :param request:
        :param view:

        """
        return request.user.role == "agent"
