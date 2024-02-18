#!/usr/bin/env python3

"""Contains Apartment views"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rental.serializers.apartment import (
    ApartmentSerializer,
    Apartment,
    ApartmentImage,
    ApartmentImageSerializer
)


class AddApartmentView(APIView):
    """
    Add apartment view
    """

    def post(self, reqquest, *args, **kwargs):
        """
        Add a new apartment
        @param reqquest: The request object
        @param args: The args
        @param kwargs: The keyword args
        @return: The response
        """
        serializer = ApartmentSerializer(data=reqquest.data)
        if serializer.is_valid():
            Apartment.custom_save(**serializer.validated_data)
            images = reqquest.FILES.getlist('images')
            for image in images:
                serialized_image = ApartmentImageSerializer(data={'apartment': serializer.instance.id, 'image': image})
                if serialized_image.is_valid():
                    ApartmentImage.custom_save(**serialized_image.validated_data)
                else:
                    return Response({
                        'error': serialized_image.errors,
                        'status': status.HTTP_400_BAD_REQUEST
                    })
            return Response({
                'message': 'Apartment added successfully',
                'apartment_images': [image.image.url for image in
                                     ApartmentImage.filter_objects(apartment=serializer.instance.id)],
                'status': status.HTTP_201_CREATED
            })
        return Response({
            'error': serializer.errors,
            'status': status.HTTP_400_BAD_REQUEST
        })
