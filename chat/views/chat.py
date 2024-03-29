#!/usr/bin/env python3

"""Chat views."""


from rest_framework import generics, status, views
from chat.serializers.chat import MessageSerializer, Message
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



class MessageListViiew(generics.ListCreateAPIView):
    """Message list view."""

    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        sender = self.request.user
        receiver = self.kwargs["receiver"]
        return Message.filter_objects(sender=sender, receiver=receiver)


class SendMessageView(views.APIView):
    """Send message view."""
    
    def post(self, request, receiver):
        sender = request.user
        receiver = receiver
        message = request.data.get("message", "")
        if not message:
            return Response({"message": "Message cannot be empty"}, status=status.HTTP_400_BAD_REQUEST)
        if sender == receiver:
            return Response({"message": "You cannot send a message to yourself"}, status=status.HTTP_400_BAD_REQUEST)
        Message.custom_save(sender=sender, receiver=receiver, message=message)
        return Response({          
            "message": "Message sent",
            "status": status.HTTP_201_CREATED
        })