#!/usr/bin/env python3

"""Contains custom permissions"""

from rest_framework.permissions import BasePermission
from rest_framework.response import Response


class IsOwner(BasePermission):
    """
    Custom permission to only allow owners to access the view.
    """

    def has_permission(self, request, view):
        if request.user.role == 'owner':
            return True
        return Response({
            'error': "You don't have the necessary permission to do this",
            'status': 403
        })


class IsTenant(BasePermission):
    """
    Custom permission to only allow tenants to access the view.
    """

    def has_permission(self, request, view):
        if request.user.role == 'tenant':
            return True
        return Response({
            'error': "You don't have the necessary permission to do this",
            'status': 403
        })


class IsAgent(BasePermission):
    """
    Custom permission to only allow agents to access the view.
    """

    def has_permission(self, request, view):
        if request.user.role == 'agent':
            return True
        return Response({
            'error': "You don't have the necessary permission to do this",
            'status': 403
        })
