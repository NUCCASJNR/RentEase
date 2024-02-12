#!/usr/bin/env python3

"""
Contains the apartment model for the rental app
"""


from rental.models.user import MainUser, BaseModel, models


class Apartment(BaseModel):
    """
    The apartment model
    """
    AVAILABILITY_STATUS = (
        ('available', 'Available'),
        ('pending', 'Pending'),
        ('rented', 'Rented'),
    )
    address = models.CharField(max_length=100, null=False, blank=False)
    owner = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='apartments')
    description = models.TextField(null=False, blank=False)
    number_of_rooms = models.IntegerField(null=False, blank=False)
    number_of_bathrooms = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    amenities = models.JSONField(null=True, blank=True)
    availability_status = models.CharField(max_length=10, choices=AVAILABILITY_STATUS, default='pending')

    class Meta:
        db_table = 'apartments'
