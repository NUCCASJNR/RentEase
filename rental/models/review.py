#!/usr/bin/env python3

"""Contains the report model for the rental app"""

from rental.models.user import BaseModel, models, MainUser
from rental.models.apartment import Apartment


class ApartmentReview(BaseModel):
    """
    The apartment review model
    """
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField(null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'apartment_reviews'
# Path: rental/models/review.py
