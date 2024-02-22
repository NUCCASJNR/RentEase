#!/usr/bin/env python3

"""Contains review booking related serializers"""


from rest_framework import serializers
from rental.models.booking import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
