#!/usr/bin/env python3
"""Contains Apartment views"""
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rental.serializers.apartment import (
    Apartment,
    ApartmentImage,
    ApartmentSerializer,
    ApartmentImageSerializer
)
from rental.utils.permissions import IsOwner


class AddApartmentView(APIView):
    """Add apartment view"""

    permission_classes = [IsAuthenticated, IsOwner]

    def post(self, request, *args, **kwargs):
        """Add a new apartment

        :param request: The request object
        :param args: The args
        :param kwargs: The keyword args
        :returns: The response

        """
        current_user = request.user
        serializer = ApartmentSerializer(data=request.data)
        if serializer.is_valid():
            images = request.FILES.getlist("images")
            if len(images) > 5:
                return Response({
                    "error": "You can only add a maximum of 5 images",
                    "status": status.HTTP_400_BAD_REQUEST,
                })
            apartment = Apartment.custom_save(owner=current_user,
                                              **serializer.validated_data)
            for image in images:
                serialized_image = ApartmentImageSerializer(
                    data={
                        "apartment": apartment.id,
                        "image": image
                    })
                if serialized_image.is_valid():
                    ApartmentImage.custom_save(
                        **serialized_image.validated_data)
                else:
                    return Response({
                        "error": serialized_image.errors,
                        "status": status.HTTP_400_BAD_REQUEST,
                    })
            return Response({
                "message": "Apartment added successfully",
                "apartment": {
                    "address":
                    apartment.address,
                    "description":
                    apartment.description,
                    "number_of_rooms":
                    apartment.number_of_rooms,
                    "number_of_bathrooms":
                    apartment.number_of_bathrooms,
                    "price":
                    apartment.price,
                    "amenities":
                    apartment.amenities,
                    "availability_status":
                    apartment.availability_status,
                    "images": [
                        image.image.url
                        for image in ApartmentImage.filter_objects(
                            apartment=apartment.id)
                    ],
                },
                "status": status.HTTP_201_CREATED,
            })
        return Response({
            "error": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        })
