#!/usr/bin/env python3

"""
Contains the apartment model for the rental app
"""


from rental.models.user import BaseModel, MainUser, models


def apartment_image_path(instance, filename):
    """The path for the apartment image

    :param instance: The instance of the apartment
    :param filename: The name of the file
    :returns: The path

    """
    return f"apartments/{instance.id}/{filename}"


class Apartment(BaseModel):
    """The apartment model"""

    AVAILABILITY_STATUS = (
        ("available", "Available"),
        ("pending", "Pending"),
        ("rented", "Rented"),
    )
    address = models.CharField(max_length=100, null=False, blank=False)
    owner = models.ForeignKey(
        MainUser, on_delete=models.CASCADE, related_name="apartments"
    )
    description = models.TextField(null=False, blank=False)
    number_of_rooms = models.IntegerField(null=False, blank=False)
    number_of_bathrooms = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False
    )
    amenities = models.JSONField(null=True, blank=True)
    availability_status = models.CharField(
        max_length=10, choices=AVAILABILITY_STATUS, default="pending"
    )

    class Meta:
        """ """
        db_table = "apartments"


class ApartmentImage(BaseModel):
    """The apartment image model"""

    apartment = models.ForeignKey(
        Apartment, on_delete=models.CASCADE, related_name="images"
    )
    image_url = models.URLField(null=False, blank=False)
    is_video = models.BooleanField(default=False)

    class Meta:
        """ """
        db_table = "apartment_images"
