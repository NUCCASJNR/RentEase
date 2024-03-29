#!/usr/bin/env python3
"""contains all the authentication related views"""
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from rental.models.user import hash_password
from rental.models.user import MainUser
from rental.serializers.auth import EmailVerificationSerializer
from rental.serializers.auth import LoginSerializer
from rental.serializers.auth import SignUpSerializer
from rental.utils.tasks import send_verification_email_async, EmailUtils
from rental.utils.redis_utils import RedisClient


class SignUpView(viewsets.ModelViewSet):
    """Signup View"""

    serializer_class = SignUpSerializer
    queryset = MainUser.objects.all()

    def create(self, request, *args, **kwargs):
        """Create a new user"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            verification_code = EmailUtils.generate_verification_code()
            hashed_password = hash_password(
                serializer.validated_data["password"])
            serializer.validated_data["password"] = hashed_password
            user = MainUser.custom_save(**serializer.validated_data,
                                        verification_code=verification_code)
            send_verification_email_async(user, verification_code)
            return Response({
                "message":
                    "You have successfully signed up. Please check your"
                    " email for the verification code",
                "status":
                    status.HTTP_201_CREATED,
            })
        else:
            errors = serializer.errors
            if "username" and "email" in errors:
                errors = {
                    "error": "User with this email and username already exists",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            if "email" in errors and errors["email"][0] == "main user with this email already exists.":
                errors = {
                    "error": "User with this email already exists",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            if "username" in errors and errors["username"][0] == "main user with this username already exists.":
                errors = {
                    "error": "User with this username already exists",
                    "status": status.HTTP_400_BAD_REQUEST
                }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class EmailVerficationView(APIView):
    """View for verifying user's email address"""

    serializer_class = EmailVerificationSerializer

    def post(self, request, *args, **kwargs):
        """Create a new user

        :param request: The request object
        :param args: The args
        :param kwargs: The keyword args
        :returns: The response

        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data["verification_code"]
            user = MainUser.custom_get(**{"verification_code": code})
            key = None
            if user is not None:
                key = f"user_id:{user.id}:{code}"
                if user.is_verified:
                    return Response({
                        "message": "Your account has already been verified",
                        "status": 200,
                    })
            redis_cli = RedisClient()
            if user and redis_cli.get_key(key):
                MainUser.custom_update(
                    filter_kwargs={"verification_code": code},
                    update_kwargs={"is_verified": True},
                )
                redis_cli.delete_key(key)
                return Response({
                    "message":
                    "Your Account has been successfully verified, You can now login!",
                    "status": status.HTTP_200_OK,
                })
            return Response({
                "error": "Invalid or expired verification code",
                "status": status.HTTP_400_BAD_REQUEST,
            })
        return Response({
            "error": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        })


class LoginView(APIView):
    """View for logging in a user"""

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """Log in a user

        :param request: The request object
        :param args: The args
        :param kwargs: The keyword args
        :param *args:
        :param **kwargs:
        :returns: The response

        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if not user.is_verified:
                    return Response({
                        "error": "You need to verify your account to login",
                        "status": status.HTTP_400_BAD_REQUEST,
                    })
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return Response({
                    "message": "You have successfully logged in",
                    "access_token": str(refresh.access_token),
                    "status": status.HTTP_200_OK,
                })
            return Response({
                "error": "Invalid email or password",
                "status": status.HTTP_400_BAD_REQUEST,
            })
        return Response({
            "error": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST
        })
