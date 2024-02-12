#!/usr/bin/env python3

"""
Contains the booking model for the rental app
"""

from rental.models.apartment import Apartment, BaseModel, models, MainUser


class Booking(BaseModel):
    """
    The booking model
    """
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    status = models.CharField(max_length=10, default='pending')

    class Meta:
        db_table = 'bookings'
# Path: rental/models/agent.py
