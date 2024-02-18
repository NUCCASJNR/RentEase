#!/usr/bin/env python3

"""Contains the apartment serializer"""

from rest_framework import serializers
from rental.models.apartment import Apartment, ApartmentImage


class ApartmentSerializer(serializers.ModelSerializer):
    """
    The apartment serializer
    """
    amenities = serializers.JSONField(required=False)

    class Meta:
        model = Apartment
        fields = ('address', 'owner', 'description', 'number_of_rooms', 'number_of_bathrooms', 'price',
                  'amenities'
                  )
