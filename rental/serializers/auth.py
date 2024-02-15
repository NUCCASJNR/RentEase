#!/usr/bin/env python3

"""contains authentication related serializers"""

from rest_framework import serializers
from rental.models.user import MainUser


class SignUpSerializer(serializers.ModelSerializer):
    """
    Signup serializer
    """

    class Meta:
        model = MainUser
        fields = ('email', 'password', 'first_name', 'last_name', 'role', 'username')


class EmailVerificationSerializer(serializers.ModelSerializer):
    """
    Email verification Serializer
    """

    class Meta:
        model = MainUser
        fields = ('verification_code', )


class LoginSerializer(serializers.Serializer):
    """
    Login serializer
    """

    class Meta:
        model = MainUser
        fields = ('email', 'password')
