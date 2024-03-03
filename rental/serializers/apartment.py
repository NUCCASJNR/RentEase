#!/usr/bin/env python3
"""Contains the apartment serializer"""
from rest_framework import serializers

from rental.models.apartment import Apartment
from rental.models.apartment import ApartmentImage


class ApartmentSerializer(serializers.ModelSerializer):
    """The apartment serializer"""

    amenities = serializers.JSONField(required=False)
    image_urls = serializers.SerializerMethodField()

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
            "image_urls",
        )

    def get_image_urls(self, obj):
        """Custom method to get image URLs

        :param obj:

        """
        print(obj.id)
        images = ApartmentImage.objects.filter(apartment=obj.id)
        if images is not None:
            # Extract URLs of all images
            image_urls = [
                ApartmentImage.to_dict(image)["image_url"] for image in images
            ]
            return image_urls
        else:
            return []


class ApartmentImageSerializer(serializers.ModelSerializer):
    """The apartment image serializer"""

    class Meta:
        """ """

        model = ApartmentImage
        fields = ("apartment", "image_url")
