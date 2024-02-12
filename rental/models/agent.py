#!/usr/bin/env python3

"""Contains the agent model for the rental app"""

from rental.models.user import BaseModel, models, MainUser


class Agent(BaseModel):
    """
    The agent model
    """
    agent = models.OneToOneField(MainUser, on_delete=models.CASCADE, related_name='agent')
    contact_information = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'agents'
