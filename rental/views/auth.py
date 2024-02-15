#!/usr/bin/env python3

"""contains all the authentication related views"""

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rental.models.user import MainUser, _hash_password
from rental.serializers.auth import SignUpSerializer
from rental.utils.email_utils import EmailUtils
from rental.utils.redis_utils import RedisClient


class SignUpView(viewsets.ModelViewSet):
    """
    Signup View
    """
    serializer_class = SignUpSerializer
    queryset = MainUser.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Create a new user
        @param request: The request object
        @param args: The args
        @param kwargs: The keyword args
        @return: The response
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            verification_code = EmailUtils.generate_verification_code()
            if MainUser.custom_get(**{'email': serializer.validated_data['email']}):
                return Response({'error': 'User with this email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if MainUser.custom_get(**{'username': serializer.validated_data['username']}):
                return Response({'error': 'User with this username already exists'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.validated_data['password'] = _hash_password(serializer.validated_data['password'])
            user = MainUser.custom_save(**serializer.validated_data, verification_code=verification_code)
            EmailUtils.send_verification_email(user, verification_code)
            return Response({
                'message': 'You have successfully signed up. Please check your'
                           ' email for the verification code',
                'status': status.HTTP_201_CREATED
            })
        return Response({
            'error': serializer.errors,
            'status': status.HTTP_400_BAD_REQUEST
        })
