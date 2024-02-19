#!/usr/bin/env python3

"""Chat serializers."""


from rest_framework import serializers
from chat.models.chat import Message


class MessageSerializer(serializers.ModelSerializer):
    """Message serializer."""

    class Meta:
        """Meta class."""

        model = Message
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at"]
