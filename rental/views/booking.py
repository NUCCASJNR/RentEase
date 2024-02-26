#!/usr/bin/env python3
"""Contains all booking related views"""
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rental.serializers.booking import Booking
from rental.serializers.booking import BookingSerializer


class BookReviewView(APIView):
    """View for booking a review for an apartment"""
