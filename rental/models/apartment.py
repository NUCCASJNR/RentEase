#!/usr/bin/env python3

"""
Contains the apartment model for the rental app
"""

from rental.models.user import MainUser, BaseModel, models
from cloudinary.models import CloudinaryField


def apartment_image_path(instance, filename):
    """
    The path for the apartment image
    @param instance: The instance of the apartment
    @param filename: The name of the file
    @return: The path
    """
    return f'apartments/{instance.id}/{filename}'


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
    agent= models.ForeignKey(MainUser, on_delete=models.SET_NULL,
                                       related_name='assigned_apartment', null=True)
    description = models.TextField(null=False, blank=False)
    number_of_rooms = models.IntegerField(null=False, blank=False)
    number_of_bathrooms = models.IntegerField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    amenities = models.JSONField(null=True, blank=True)
    availability_status = models.CharField(max_length=10, choices=AVAILABILITY_STATUS, default='pending')

    class Meta:
        db_table = 'apartments'
    
    


class ApartmentImage(BaseModel):
    """
    The apartment image model
    """
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='images')
    image = CloudinaryField('image', null=True, blank=True)
    is_video = models.BooleanField(default=False)

    class Meta:
        db_table = 'apartment_images'
    
    def style(self):
        """Convert the ApartmentImage object to a dictionary"""
        return {
            'image_url': self.image.url if self.image else None,
            'is_video': self.is_video,
            # Add other fields as needed
        }