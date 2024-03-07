#!/usr/bin/env python3

"""Contains Apartment views"""
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from RentEase import celery_app
from rental.models.user import MainUser as User

from rental.serializers.apartment import (
    Apartment,
    ApartmentSerializer,
)
from rental.utils.permissions import IsOwner


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
        print(serializer.initial_data)
        current_user = request.user
        if serializer.is_valid():
            print(serializer.validated_data)
            images = request.FILES.getlist("images")
            if len(images) > 5:
                return Response({
                    "error": "You can only add a maximum of 5 images",
                    "status": status.HTTP_400_BAD_REQUEST,
                })
            agent = User.custom_get(email=serializer.validated_data.get('agent_assigned'))
            serializer.validated_data.pop('agent_assigned')
            image_path = [image.read() for image in images]
            apartment = Apartment.custom_save(owner=current_user,
                                              **serializer.validated_data, assigned_agent_id=agent.id)
            apartment_id = apartment.id
            agent_email = agent.email
            agent_username = agent.username
            apartment_details = {
                'address': apartment.address,
                'price': apartment.price,
                'number_of_rooms': apartment.number_of_rooms,
                'number_of_bathrooms': apartment.number_of_bathrooms,
                'availability_status': apartment.availability_status,
            }
            celery_app.send_task('rental.utils.tasks.send_assigned_apartment_email_async',
                                 args=(agent_email, agent_username, apartment_details))
            celery_app.send_task('rental.utils.tasks.async_upload_images',
                                 args=(str(apartment_id), image_path))
            return Response({
                "message": "Apartment added successfully",
                "status": status.HTTP_201_CREATED,
            })
        return Response({
            "error": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        })

    def update(self, request, *args, **kwargs):
        """
        View for updating an apartment
        @param request:
        @param args:
        @param kwargs:
        @return:
        """

