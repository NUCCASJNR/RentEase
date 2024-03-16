#!/usr/bin/env python3
"""Contains the apartment serializer"""
from rest_framework import serializers

from rental.models.apartment import Apartment
from rental.models.apartment import ApartmentImage
from rental.models.booking import Booking

class ApartmentSerializer(serializers.ModelSerializer):
    """The apartment serializer"""

    amenities = serializers.JSONField(required=False)
    agent = serializers.EmailField(required=True)
    images = serializers.SerializerMethodField()
    id = serializers.UUIDField(read_only=True)

    class Meta:
        """ """
        model = Apartment
        fields = (
            "address",
            "description",
            "number_of_rooms",
            "number_of_bathrooms",
            "price",
            "amenities",
            "images",
            "agent",
            "id"
        )

    def get_images(self, obj):
        """Custom method to get image"""
        images = ApartmentImage.objects.filter(apartment=obj.id)
        if images.exists():
            image_styles = [image.style() for image in images]
            image_urls = [image_style['image_url'] for image_style in image_styles]
            return image_urls
        else:
            return []



class ApartmentImageSerializer(serializers.ModelSerializer):
    """The apartment image serializer"""

    class Meta:
        """ """
        model = ApartmentImage
        fields = ("apartment", "image")




class BookingSerializer(serializers.ModelSerializer):
    apartment = serializers.UUIDField(required=True)

    class Meta:
        model = Booking
        fields = ('date', 'apartment')
