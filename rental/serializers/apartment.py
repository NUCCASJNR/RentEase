#!/usr/bin/env python3
"""Contains the apartment serializer"""
from rest_framework import serializers

from rental.models.apartment import Apartment
from rental.models.apartment import ApartmentImage


class ApartmentSerializer(serializers.ModelSerializer):
    """The apartment serializer"""

    amenities = serializers.JSONField(required=False)
    agent_assigned = serializers.EmailField(required=True)
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
            "agent_assigned",
        )

    def get_image_urls(self, obj):
        """Custom method to get image URLs"""
        print(obj.id)
        images = ApartmentImage.objects.filter(apartment=obj.id)
        if images is not None:
            image_urls = [ApartmentImage.to_dict(image)['image_url'] for image in images]
            return image_urls
        else:
            return []

    # def get_agent_assigned(self, obj):
    #     """Custom method to get the agent assigned to the apartment"""
    #     agent = obj.assigned_agent
    #     if agent is not None:
    #         return {
    #             "email": agent.email,
    #             "first_name": agent.first_name,
    #             "last_name": agent.last_name
    #         }
    #     else:
    #         return None


class ApartmentImageSerializer(serializers.ModelSerializer):
    """The apartment image serializer"""

    class Meta:
        """ """
        model = ApartmentImage
        fields = ("apartment", "image")
