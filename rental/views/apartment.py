#!/usr/bin/env python3

"""Contains Apartment views"""
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rental.serializers.apartment import (
    Apartment,
    ApartmentSerializer,
)
from rental.utils.permissions import IsOwner
from rental.utils.tasks import upload_apartment_images_task


class AddApartmentViewset(viewsets.ModelViewSet):
    queryset = Apartment.get_all()
    serializer_class = ApartmentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def create(self, request, *args, **kwargs):
        """
        View for creating apartment
        @param request: request parameter
        @param args: request args
        @param kwargs: request kwrags
        @return: The details of the apartment created
        """
        serializer = self.serializer_class(data=request.data)
        current_user = request.user
        if serializer.is_valid():
            images = request.FILES.getlist("images")
            if len(images) > 5:
                return Response({
                    "error": "You can only add a maximum of 5 images",
                    "status": status.HTTP_400_BAD_REQUEST,
                })
            image_path = [image.read() for image in images]
            apartment = Apartment.custom_save(owner=current_user,
                                              **serializer.validated_data)
            upload_apartment_images_task.delay(str(apartment.id), image_path)
            return Response({
                "message": "Apartment added successfully",
                "status": status.HTTP_201_CREATED,
            })
        return Response({
            "error": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        })

