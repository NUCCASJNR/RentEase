#!/usr/bin/env python3
"""Contains the apartment serializer"""
from rest_framework import serializers

from rental.models.apartment import Apartment
from rental.models.apartment import ApartmentImage


class ApartmentSerializer(serializers.ModelSerializer):
    """The apartment serializer"""

    amenities = serializers.JSONField(required=False)
    agent = serializers.EmailField(required=True)
    images = serializers.SerializerMethodField()

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
            "agent"
        )

    def get_images(self, obj):
        """Custom method to get image"""
        images = ApartmentImage.objects.filter(apartment=obj.id)
        if images.exists():
            print([ApartmentImage.to_dict(image) for image in images])
            image_urls = [ApartmentImage.to_dict(image)['url'] for image in images]
            return image_urls
        else:
            return []
        


class ApartmentImageSerializer(serializers.ModelSerializer):
    """The apartment image serializer"""

    class Meta:
        """ """
        model = ApartmentImage
        fields = ("apartment", "image")
